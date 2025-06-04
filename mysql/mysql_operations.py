import csv
import mysql.connector
from mysql.connector import Error


class MySQLDatabase:
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """建立数据库连接"""
        try:
            config = {
                'host': self.host,
                'user': self.user,
                'password': self.password,
            }
            if self.database:
                config['database'] = self.database

            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f'已连接到MySQL服务器版本: {db_info}')
                if self.database:
                    print(f'已选择数据库: {self.database}')
                return True
        except Error as e:
            print(f'连接数据库时发生错误: {e}')
            return False

    def disconnect(self):
        """断开数据库连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('已断开数据库连接')

    def create_database(self, db_name):
        """创建数据库"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法创建数据库')
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f'成功创建数据库: {db_name}')
            return True
        except Error as e:
            print(f'创建数据库时发生错误: {e}')
            return False
        finally:
            if cursor:
                cursor.close()

    def create_table(self, table_name, columns_definition):
        """创建表"""
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

    def upload_csv(self, table_name, csv_file, delimiter=','):
        """从 CSV 文件导入数据到指定表"""
        if not self.connection or not self.connection.is_connected():
            print('未连接到数据库，无法上传 CSV 文件')
            return False

        try:
            cursor = self.connection.cursor()
            with open(csv_file, 'r') as file:
                csv_data = csv.reader(file, delimiter=delimiter)
                headers = next(csv_data)  # 获取表头

                # 生成列名和占位符
                placeholders = ', '.join(['%s'] * len(headers))
                columns = ', '.join([f'`{header}`' for header in headers])
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                # 批量插入数据
                batch_size = 1000
                batch = []
                for row in csv_data:
                    batch.append(tuple(row))
                    if len(batch) >= batch_size:
                        cursor.executemany(insert_query, batch)
                        batch = []

                # 插入剩余数据
                if batch:
                    cursor.executemany(insert_query, batch)

            self.connection.commit()
            print(f'成功将 CSV 文件 {csv_file} 导入到表 {table_name}')
            return True
        except Error as e:
            print(f'上传 CSV 文件时发生错误: {e}')
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()


# 使用示例
if __name__ == "__main__":
    # 数据库连接配置 - 不指定数据库名，用于创建数据库
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Juvenile686',
    }

    # 创建数据库连接（不指定数据库）
    db_creator = MySQLDatabase(**db_config)
    if db_creator.connect():
        # 创建数据库
        db_name = 'excel_test'
        if db_creator.create_database(db_name):
            db_creator.disconnect()

            # 连接到新创建的数据库
            db_config['database'] = db_name
            db = MySQLDatabase(**db_config)
            if db.connect():
                # 创建示例表
                table_name = 'energy_data'
                columns_definition = """
                    `temperature` DECIMAL(5,2) NOT NULL,
                    `hour` INT NOT NULL,
                    `is_weekend` TINYINT(1) NOT NULL,
                    `energy` DECIMAL(5,2) NOT NULL
                """
                db.create_table(table_name, columns_definition)

                # 上传 CSV 文件示例
                csv_file = 'demoData.csv'  # 确保文件存在且格式正确
                db.upload_csv(table_name, csv_file)

                # 断开数据库连接
                db.disconnect()
        else:
            db_creator.disconnect()