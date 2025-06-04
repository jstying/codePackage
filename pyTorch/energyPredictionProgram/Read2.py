from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import torch.nn as nn
import os
import sys
import io
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'} # 仅允许csv文件

# 上传文件将存储在项目根目录下的 uploads 文件夹中
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 如果uploads目录不存在，创建目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# CSVDataset类
class CSVDataset(Dataset):
    def __init__(self, features, labels):
        # 转换成torch tensor
        self.X = torch.tensor(features, dtype=torch.float32)
        self.y = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        # 数据集的总样本数
        return len(self.X)

    def __getitem__(self, idx):
        # 根据索引获取样本
        return self.X[idx], self.y[idx]


# readCSV函数
def readCSV(csv_fname):
    df = pd.read_csv(csv_fname)
    rows, columns = df.shape
    if columns < 2:
        raise ValueError(f"数据列数不足（至少需要2列），实际列数：{columns}")
    # 读取前三列
    X = df.iloc[:, :-1].values
    # 读取最后一列
    y = df.iloc[:, -1].values
    return CSVDataset(X, y)


# split_dataset函数
def split_dataset(dataset, train_ratio=0.8, seed=42):
    '''划分数据集为2个子集：训练集和验证集'''
    train_size = int(train_ratio * len(dataset))
    val_size = len(dataset) - train_size
    generator = torch.Generator().manual_seed(seed)
    return random_split(dataset, [train_size, val_size], generator=generator)


# create_dataloaders函数
def create_dataloaders(train_dataset, val_dataset, batch_size=32):
   '''返回 2 个数据加载器'''
   train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
   val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
   return train_loader, val_loader


# EnergyPredictor类
class EnergyPredictor(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        pass

    def forward(self, x):
        pass

# 辅助函数：检查文件扩展名是否合法（如 .csv）
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 主页 - 文件上传表单
# GET 请求：返回文件上传表单页面
# POST 请求：处理表单提交的文件数据
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # 处理POST请求
    if request.method == 'POST':
        # 检查文件是否存在于请求中
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        # 检查用户是否选择了文件
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        # 验证文件类型并保存
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            try:
                # 调用你的数据处理逻辑
                dataset = readCSV(file_path)
                train_dataset, val_dataset = split_dataset(dataset)
                train_loader, val_loader = create_dataloaders(train_dataset, val_dataset)

                # 初始化模型
                input_size = dataset.X.shape[1]
                # model = EnergyPredictor(input_size)

                # 返回成功信息和数据统计给前端
                result = {
                    "status": "success",
                    "message": "数据加载成功",
                    "total_samples": len(dataset),
                    "train_samples": len(train_dataset),
                    "val_samples": len(val_dataset),
                    "input_features": input_size
                }
                return jsonify(result)

            except Exception as e:
                return jsonify({"error": str(e)}), 500
    #处理GET请求
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 监听所有可用网络接口