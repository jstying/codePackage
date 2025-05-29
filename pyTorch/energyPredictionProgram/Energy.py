from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import traceback

app = Flask(__name__)

# 加载预训练的模型
try:
    model = joblib.load('energy_prediction_model.pkl')  # 加载训练好的模型
    print("模型加载成功")
except Exception as e:
    print(f"模型加载失败: {e}")
    model = None


# 数据预处理函数
def preprocess_data(input_data):
    """将输入数据转换为模型需要的格式"""
    try:
        # 创建特征DataFrame
        df = pd.DataFrame([input_data])

        # 添加时间特征（示例：从时间戳提取小时、星期几等）
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.dayofweek
            df['month'] = df['timestamp'].dt.month
            # 可以添加更多时间特征如是否周末、是否节假日等

        # 确保所有需要的特征都存在
        required_features = ['temperature', 'humidity', 'hour', 'day_of_week', 'month']
        for feature in required_features:
            if feature not in df.columns:
                df[feature] = 0  # 填充默认值

        # 返回模型需要的特征矩阵
        return df[required_features]

    except Exception as e:
        print(f"数据预处理错误: {e}")
        traceback.print_exc()
        return None


# 预测API
@app.route('/predict', methods=['POST'])
def predict():
    """接收能耗相关数据并返回预测结果"""
    try:
        # 检查模型是否已加载
        if model is None:
            return jsonify({"error": "模型未成功加载"}), 500

        # 获取请求数据
        data = request.json

        # 验证请求数据
        if not data:
            return jsonify({"error": "请求数据为空"}), 400

        # 数据预处理
        processed_data = preprocess_data(data)
        if processed_data is None:
            return jsonify({"error": "数据预处理失败"}), 400

        # 进行预测
        prediction = model.predict(processed_data)

        # 返回预测结果
        return jsonify({
            "status": "success",
            "prediction": prediction[0],  # 假设返回单个预测值
            "timestamp": datetime.now().isoformat(),
            "input_data": data
        })

    except Exception as e:
        print(f"预测过程出错: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# 批量预测API
@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """接收多个能耗数据并返回批量预测结果"""
    try:
        if model is None:
            return jsonify({"error": "模型未成功加载"}), 500

        data = request.json

        if not data or not isinstance(data, list):
            return jsonify({"error": "需要提供数据列表"}), 400

        predictions = []
        for item in data:
            processed_data = preprocess_data(item)
            if processed_data is not None:
                pred = model.predict(processed_data)
                predictions.append({
                    "input": item,
                    "prediction": pred[0]
                })

        return jsonify({
            "status": "success",
            "total_predictions": len(predictions),
            "results": predictions,
            "timestamp": datetime.now().isoformat()
        })

    except Exception as e:
        print(f"批量预测出错: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# 模型信息API
@app.route('/model_info', methods=['GET'])
def model_info():
    """返回模型的基本信息"""
    try:
        if model is None:
            return jsonify({"error": "模型未成功加载"}), 500

        # 返回模型信息（根据实际模型类型调整）
        return jsonify({
            "model_type": type(model).__name__,
            "model_params": model.get_params(),
            "status": "available",
            "timestamp": datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)