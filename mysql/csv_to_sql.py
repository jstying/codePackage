from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import torch.nn as nn
import os
import sys
import io
from werkzeug.utils import secure_filename
import csv
import mysql.connector
from mysql.connector import Error  #与 MySQL 数据库交互过程出现的错误


class MySQLDatabase:
    # 与 MySQL 数据库连接并进行操作
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """建立数据库连接，连接成功/失败 返回 True/False"""
        try:
            # config dict 存储连接数据库所用参数
            config = {
                'host': self.host,
                'user': self.user,
                'password': self.password,
            }
            if self.database:    # 若已指定数据库
                config['database'] = self.database

            # 解包config dict，连接数据库，self.connection成为实例
            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                db_info = self.connection.server_info
                print(f'已连接到MySQL服务器版本: {db_info}')
                if self.database:
                    print(f'已选择数据库: {self.database}')
                return True
        except Error as e:
            print(f'连接数据库时发生错误: {e}')
            return False

    def disconnect(self):
        """断开数据库连接"""
        # 连接对象存在，且被连接时
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('已断开数据库连接')

    def create_database(self, db_name):
        """传入数据库名称，创建数据库，创建成功/失败 返回 True/False"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法创建数据库')
            return False

        try:
            # 创建游标对象，用来执行SQL语句
            cursor = self.connection.cursor()
            # ci 大小写不敏感/同义
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f'成功创建数据库: {db_name}')
            return True
        except Error as e:
            print(f'创建数据库时发生错误: {e}')
            return False
        finally: # try后执行关闭游标（必须
            if cursor:
                cursor.close()

    def drop_database(self, db_name):
        """删除指定的数据库，成功/失败 返回 True/False"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法删除数据库')
            return False

        # 安全检查：防止意外删除重要数据库
        if db_name.lower() in ['sakila', 'world', 'sys']:
            print(f'拒绝删除系统数据库: {db_name}')
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
            print(f'成功删除数据库: {db_name}')
            return True
        except Error as e:
            print(f'删除数据库时发生错误: {e}')
            return False
        finally:
            if cursor:
                cursor.close()

    def create_table(self, table_name, columns_definition):
        """传入表名称，列名和数据类型，创建表创建成功/失败 返回 True/False"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法创建表')
            return False

        try:
            cursor = self.connection.cursor()
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
            cursor.execute(create_table_query)
            print(f'成功创建表 {table_name}')
            return True
        except Error as e:
            print(f'创建表时发生错误: {e}')
            return False
        finally:
            if cursor:
                cursor.close()

    # delimiter csv分隔符默认，
    def upload_csv(self, table_name, csv_file, delimiter=','):
        """从 CSV 文件导入数据到指定表，成功/失败 返回 True/False"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法上传 CSV 文件')
            return False

        try:
            cursor = self.connection.cursor()
            with open(csv_file, 'r') as file:
                # 解析csv文件
                csv_data = csv.reader(file, delimiter=delimiter)
                headers = next(csv_data)  # 获取表头

                # 生成列名和占位符
                placeholders = ', '.join(['%s'] * len(headers))  # %s, %s, %s
                columns = ', '.join([f'`{header}`' for header in headers])  # `id`, `name`, `age`
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                # INSERT INTO users (`temperature`, `hour`, `is_weekend`, `energy`) VALUES (%s, %s, %s)

                # 累积一定数量插入数据
                batch_size = 1000  # 每批处理1000条记录
                batch = []
                for row in csv_data:
                    batch.append(tuple(row))  # 将每行数据转为元组后添加到批次
                    if len(batch) >= batch_size:
                        cursor.executemany(insert_query, batch)  # 单次插入1000条
                        batch = []  # 清空缓冲区

                #  检查缓冲区中是否还有剩余数据, 插入剩余数据
                if batch:
                    cursor.executemany(insert_query, batch)

            self.connection.commit()  # 事务提交
            print(f'成功将 CSV 文件 {csv_file} 导入到表 {table_name}')
            return True
        except Error as e:
            print(f'上传 CSV 文件时发生错误: {e}')
            self.connection.rollback() # 撤销本次事务中所有未提交的 SQL 操作
            return False
        finally:
            if cursor:
                cursor.close()


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}  # 仅允许csv文件

# 上传文件将存储在项目根目录下的 uploads 文件夹中
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 如果uploads目录不存在，创建目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 辅助函数：检查文件扩展名是否合法（如 .csv）
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 主页 - 文件上传表单
# GET 请求：返回upload.html页面
# POST 请求：文件上传和数据库操作
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
        # 验证文件类型并保存到uploads文件夹
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # 从表单中获取sql密码名称
            sql_pwd = request.form.get('sql_pwd').strip()

            try:
                db_config = {
                    'host': 'localhost',
                    'user': 'root',
                    'password': sql_pwd,
                }

                # 创建数据库实例，通过解包dict
                # 等同于MySQLDatabase(host='localhost', user='root', password='xx')
                db_creator = MySQLDatabase(**db_config)
                # 连接到数据库服务器（未指定具体数据库）
                if db_creator.connect():

                    # 从表单中获取数据库名称
                    db_name = request.form.get('db_name').strip()


                    if db_creator.create_database(db_name):
                        # 断开服务器连接
                        db_creator.disconnect()
                        # 更新配置，添加新创建的数据库名
                        db_config['database'] = db_name

                        # 创建新的数据库连接
                        db = MySQLDatabase(**db_config)
                        if db.connect():
                            # 创建示例表
                            table_name = request.form.get('tb_name').strip()

                            # (5,2) 总位数：5 位（含小数点, 小数位数：2 位
                            # TINYINT(1)仅用于显示宽度
                            columns_definition = """
                                `temperature` DECIMAL(5,2) NOT NULL,
                                `hour` INT NOT NULL,
                                `is_weekend` TINYINT(1) NOT NULL,
                                `energy` DECIMAL(5,2) NOT NULL
                            """
                            db.create_table(table_name, columns_definition)

                            # 上传 CSV 文件
                            db.upload_csv(table_name, file_path)

                            # 断开数据库连接
                            db.disconnect()

                            # 返回成功信息和数据统计给前端
                            result = {
                                "status": "success",
                                "message": "数据加载成功并已存入数据库",
                            }
                            return jsonify(result)  # 返回给前端

            except Exception as e:
                return jsonify({"error": str(e)}), 500
    # 处理GET请求 展示页面
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 监听所有可用网络接口