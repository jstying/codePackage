import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import torch.nn as nn
import os
import sys


class CSVDataset(Dataset):  # 继承Dataset类
   def __init__(self, features, labels): # 转成torch tensor
      self.X = torch.tensor(features, dtype=torch.float32)
      self.y = torch.tensor(labels, dtype=torch.float32)

   def __len__(self):  # 数据集的总样本数
      return len(self.X)

   def __getitem__(self, idx):  # 根据索引获取样本
      return self.X[idx], self.y[idx]



def readCSV(csv_fname):
   # 读取 CSV 文件为dataFrame对象 df
   df = pd.read_csv(csv_fname)

   # 行数和列数
   rows, columns = df.shape
   if columns < 2:
      raise ValueError(f"数据列数不足（至少需要2列），实际列数：{columns}")
   # 读取前三列
   X = df.iloc[:, :-1].values
   # 读取最后一列
   y = df.iloc[:, -1].values

   # 打印数据基本信息
   print("数据基本信息：")
   df.info()

   # 创建数据集
   return CSVDataset(X, y)


def split_dataset(dataset, train_ratio=0.8, seed=42):
   '''划分数据集为2个子集：训练集和验证集'''
   train_size = int(train_ratio * len(dataset))
   val_size = len(dataset) - train_size
   generator = torch.Generator().manual_seed(seed)  # 固定随机种子，确保结果可复现
   return random_split(dataset, [train_size, val_size], generator=generator)


def create_dataloaders(train_dataset, val_dataset, batch_size=32):
   '''返回 2 个数据加载器'''
   # 训练时需要随机打乱数据
   train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
   # 验证时需要固定顺序
   val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
   return train_loader, val_loader


class EnergyPredictor(nn.Module):
   def __init__(self, input_size): # 温度、时间、是否周末，input_size = 3
      super().__init__()
      pass

   def forward(self, x):
      pass






def main():
   # C:\Users\yingj\PycharmProjects\pytorchLearn\demoData.csv
   # 获取用户输入的CSV文件路径
   file_path = input("请输入CSV文件路径: ").strip()

   # 检查文件是否存在
   if not os.path.exists(file_path):
       print(f"错误：文件 '{file_path}' 不存在！")
       return

   # 检查是否为CSV文件
   if not file_path.lower().endswith('.csv'):
       print(f"错误：'{file_path}' 不是CSV文件！")
       return

   #读取
   try:
      dataset = readCSV(file_path)
      train_dataset, val_dataset = split_dataset(dataset)
      train_loader, val_loader = create_dataloaders(train_dataset, val_dataset)
   except FileNotFoundError as e:
      print(f"错误：文件不存在 - {e}")
      return 1
   except ValueError as e:
      print(f"数据格式错误 - {e}")
      return 1
   except Exception as e:
      print(f"意外错误 - {e}")
      return 1
   else:
      print("所有操作成功！")
      return 0


if __name__ == '__main__':
   sys.exit(main())

