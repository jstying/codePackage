import numpy as np
import pandas as pd

# 设置随机种子，确保结果可重现
np.random.seed(42)


# 生成更真实的模拟数据
def generate_realistic_energy_data(n_samples):
    # 创建时间序列（模拟连续的时间段）
    hours = np.sort(np.random.choice(24 * 7, n_samples, replace=False))  # 一周内随机小时
    is_weekend = (hours // 24 >= 5).astype(int)  # 5和6是周六和周日
    hour_of_day = hours % 24

    # 生成更真实的温度数据（考虑昼夜和季节变化）
    # 冬季温度范围，白天高夜间低
    base_temperature = 5 + 8 * np.sin(hour_of_day * np.pi / 12)  # 基础温度波动
    temperature = base_temperature + np.random.normal(0, 3, n_samples)  # 添加随机噪声

    # 生成更真实的能耗数据（与温度、时间相关）
    # 基础能耗（所有设备待机）
    base_energy = 20

    # 温度影响（温度过低或过高时，空调/暖气能耗增加）
    temperature_effect = np.maximum(temperature - 22, 0) * 3 + np.maximum(15 - temperature, 0) * 4

    # 时间影响（工作时间能耗高，夜间能耗低）
    time_factor = np.ones(n_samples)
    time_factor[(hour_of_day < 6) | (hour_of_day > 21)] = 0.5  # 夜间系数
    time_factor[(hour_of_day >= 9) & (hour_of_day <= 18) & (is_weekend == 0)] = 1.8  # 工作日白天系数

    # 随机波动（模拟设备随机开关）
    random_fluctuation = np.random.normal(0, 10, n_samples)

    # 计算最终能耗
    energy = base_energy + temperature_effect * time_factor + random_fluctuation
    energy = np.maximum(energy, 10)  # 确保能耗不低于最小值

    return {
        "temperature": np.round(temperature, 1),
        "hour": hour_of_day,
        "is_weekend": is_weekend,
        "energy": np.round(energy, 1)
    }


# 生成数据并保存
data = generate_realistic_energy_data(160)
df = pd.DataFrame(data)
df.to_csv("demoData.csv", index=False)
print("生成160条更真实的演示数据，字段：temperature, hour, is_weekend, energy")

# 打印数据样本预览
print("\n数据样本预览：")
print(df.head().to_string())