from flask import Flask, render_template, request, jsonify

import os

from werkzeug.utils import secure_filename
import csv
import mysql.connector
from mysql.connector import Error  #与 MySQL 数据库交互过程出现的错误
from flask import make_response
import csv


class MySQLDatabase:
    # 与 MySQL 数据库连接并进行操作
    def __init__(self, host, user, password):  #, database=None
        self.host = host
        self.user = user
        self.password = password
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

            # 解包config dict，连接数据库，self.connection成为实例
            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                db_info = self.connection.server_info
                print(f'已连接到MySQL服务器版本: {db_info}')
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


        try:
            if not self.connection or not self.connection.is_connected():
                raise ValueError('未连接到数据库，无法创建数据库')
                return False

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

    def table_exists(self, db_name, tb_name):
        """检查指定数据库中是否存在某个表"""
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return False

        try:
            cursor = self.connection.cursor()
            # 查询 information_schema.tables 系统表
            cursor.execute("""
                           SELECT TABLE_NAME
                           FROM information_schema.tables
                           WHERE TABLE_SCHEMA = %s
                             AND TABLE_NAME = %s
                           """, (db_name, tb_name))
            result = cursor.fetchone()
            return result is not None  # 存在返回 True，否则 False
        except Error as e:
            print(f"检查数据表时发生错误: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def database_exists(self, db_name):
        """检查数据库是否存在"""
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return False

        try:
            cursor = self.connection.cursor()
            # 查询 information_schema.schemata 系统表
            cursor.execute("""
                           SELECT SCHEMA_NAME
                           FROM information_schema.schemata
                           WHERE SCHEMA_NAME = %s
                           """, (db_name,))
            result = cursor.fetchone()
            return result is not None  # 存在返回 True，否则 False
        except Error as e:
            print(f"检查数据库时发生错误: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def drop_database(self, db_name):
        """删除指定的数据库，成功/失败 返回 True/False"""
        try:
            if not self.connection or not self.connection.is_connected():
                raise ValueError('未连接到数据库，无法创建数据库')
                return False

            # 安全检查：防止意外删除重要数据库
            if db_name.lower() in ['sakila', 'world', 'sys','information_schema', 'performance_schema', 'mysql']:
                raise ValueError(f'拒绝删除系统数据库: {db_name}')
                return False


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

    def drop_table(self, db_name, tb_name):
        """删除指定数据库中的表，成功/失败 返回 True/False"""
        try:
            if not self.connection or not self.connection.is_connected():
                raise ValueError('未连接到数据库，无法删除表')
                return False

            # 安全检查：防止意外删除重要系统表
            if db_name.lower() in ['sakila', 'world', 'sys','information_schema', 'performance_schema', 'mysql']:
                raise ValueError(f'拒绝删除系统表: {tb_name}')
                return False

            # 切换到指定数据库
            if not self.use_database(db_name):
                raise ValueError(f'无法切换到数据库: {db_name}')
                return False

            # 构建删除表的SQL语句，使用IF EXISTS避免表不存在时的错误
            cursor = self.connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS `{tb_name}`")
            print(f'成功删除表: {tb_name}')
            return True

        except Error as e:
            print(f'删除表时发生错误: {e}')
            return False
        finally:
            if cursor:
                cursor.close()

    def execute_query(self, query):
        """执行任意 SQL 查询"""
        if not self.connection or not self.connection.is_connected():
            raise ValueError("未连接到数据库")

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return True
        except Error as e:
            print(f"查询执行失败: {e}")
            return False
        finally:
            cursor.close()

    def use_database(self, db_name):
        """切换到指定数据库"""
        return self.execute_query(f"USE {db_name}")

    def create_table(self, table_name, columns_definition):
        """传入表名称，列名和数据类型，创建表创建成功/失败 返回 True/False"""
        try:
            if not self.connection or not self.connection.is_connected():
                raise ValueError('未连接到数据库，无法创建数据库')
                return False

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
        try:
            if not self.connection or not self.connection.is_connected():
                raise ValueError('未连接到数据库，无法创建数据库')
                return False
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

    def list_db(self, exclude_system=True):
        """获取所有数据库的列表（可选择排除系统数据库）"""
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return []

        try:
            cursor = self.connection.cursor()
            query = "SELECT SCHEMA_NAME FROM information_schema.schemata"

            # 添加过滤条件
            if exclude_system:
                query += """
                    WHERE SCHEMA_NAME NOT IN (
                        'sakila', 'world', 'sys','information_schema', 'performance_schema', 'mysql'
                    )
                """

            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Error as e:
            print(f"获取数据库列表时发生错误: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def list_tb(self, db_name):
        """获取指定数据库中所有表的列表（可选择排除系统表）"""
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return []

        try:
            cursor = self.connection.cursor()

            # 安全检查：防止意外删除重要系统表
            if db_name.lower() in ['sakila', 'world', 'sys', 'information_schema', 'performance_schema', 'mysql']:
                raise ValueError(f'拒绝展示系统数据库: {db_name}')
                return []

            # 查询指定数据库中的所有表
            query = """
                    SELECT TABLE_NAME
                    FROM information_schema.tables
                    WHERE TABLE_SCHEMA = %s \
                    """



            cursor.execute(query, (db_name,))
            return [row[0] for row in cursor.fetchall()]
        except Error as e:
            print(f"获取表列表时发生错误: {e}")
            return []
        finally:
            if cursor:
                cursor.close()


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}  # 仅允许csv文件


db_config = {
                    'host': 'localhost',
                    'user': 'root',
                    'password': None,
                }


# 上传文件将存储在项目根目录下的 uploads 文件夹中
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 如果uploads目录不存在，创建目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 辅助函数：检查文件扩展名是否合法（如 .csv）
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # 从表单中获取sql密码名称
            sql_pwd = request.form.get('sql_pwd').strip()
            if not sql_pwd:
                raise ValueError("SQL密码不能为空")



            # 创建数据库实例，通过解包dict
            db_creator = MySQLDatabase(host='localhost', user='root', password=sql_pwd)

            # 连接到数据库服务器（未指定具体数据库）
            if db_creator.connect():
                # 断开数据库连接
                db_creator.disconnect()

                # 密码
                db_config['password'] = sql_pwd

                # 返回成功信息和数据统计给前端
                result = {
                    "loginStatus": "success",
                    "message": "连接mysql成功",
                }
                return jsonify(result)  # 返回给前端
            else:
                raise ValueError("SQL密码错误")


        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
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

            try:
                db_creator = MySQLDatabase(**db_config)
                # 连接到数据库服务器（未指定具体数据库）
                if db_creator.connect():
                    # 从form中获取数据库名称
                    db_name = request.form.get('db_name').strip()
                    if not db_name:
                        raise ValueError("数据库名称不能为空")
                    if db_name.isdigit():
                        raise ValueError("数据库名不能为纯数字")
                    if db_name.lower() in ['sakila', 'world', 'sys','information_schema', 'performance_schema', 'mysql']:
                        raise ValueError(f'拒绝修改系统数据库: {db_name}')
                    if db_creator.create_database(db_name):
                        # 断开服务器连接
                        db_creator.disconnect()
                        sql_pwd = db_config['password']
                        # 创建新的数据库连接
                        db = MySQLDatabase('localhost', user='root', password=sql_pwd)
                        if db.connect():
                            # 创建示例表
                            tb_name = request.form.get('tb_name').strip()
                            if not tb_name:
                                raise ValueError("表名称不能为空")
                            if tb_name.isdigit():
                                raise ValueError("表名称不能为纯数字")

                            if db.table_exists(db_name, tb_name):
                                raise ValueError("该表已存在")

                            # (5,2) 总位数：5 位（含小数点, 小数位数：2 位
                            # TINYINT(1)仅用于显示宽度
                            columns_definition = """
                                `temperature` DECIMAL(5,2) NOT NULL,
                                `hour` INT NOT NULL,
                                `is_weekend` TINYINT(1) NOT NULL,
                                `energy` DECIMAL(5,2) NOT NULL
                            """
                            db.use_database(db_name)
                            db.create_table(tb_name, columns_definition)

                            # 上传 CSV 文件
                            db.upload_csv(tb_name, file_path)

                            # 断开数据库连接
                            db.disconnect()

                            # 返回成功信息和数据统计给前端
                            result = {
                                "status": "success",
                                "message": "数据加载成功并已存入数据库",
                            }
                            return jsonify(result)  # 返回给前端

                else:
                    raise ValueError("无法连接到SQL")


            except Exception as e:
                return jsonify({"error": str(e)}), 500
    # 处理GET请求 展示页面
    return render_template('upload.html')


@app.route('/delete_db', methods=['GET', 'POST'])
def delete_db():
    if request.method == 'POST':
        try:
            # 创建数据库操作实例
            db_creator = MySQLDatabase(**db_config)

            # 连接到数据库服务器（不指定具体数据库）
            if db_creator.connect():
                # 从表单获取要删除的数据库名称
                db_name = request.form.get('db_name').strip()

                # 验证数据库名称
                if not db_name:
                    raise ValueError("数据库名称不能为空")
                if db_name.isdigit():
                    raise ValueError("数据库名不能为纯数字")

                if not db_creator.database_exists(db_name):
                    raise ValueError("该数据库不存在")

                # 调用删除数据库的方法
                if db_creator.drop_database(db_name):
                    db_creator.disconnect()  # 断开连接
                    return jsonify({"status": "success",
                                    "message": f"数据库 {db_name} 已成功删除"})
                else:
                    raise ValueError(f"删除数据库 {db_name} 失败")
            else:
                raise ValueError("无法连接到SQL服务器")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # 处理GET请求，展示删除数据库的页面
    return render_template('delete_db.html')  # 应该渲染专门的删除页面


@app.route('/delete_tb', methods=['GET', 'POST'])
def delete_tb():
    if request.method == 'POST':
        try:
            # 创建数据库操作实例
            db_creator = MySQLDatabase(**db_config)

            # 连接到数据库服务器（不指定具体数据库）
            if db_creator.connect():
                # 从表单获取要删除的数据库名称
                db_name = request.form.get('db_name').strip()

                # 验证数据库名称
                if not db_name:
                    raise ValueError("数据库名称不能为空")
                if db_name.isdigit():
                    raise ValueError("数据库名不能为纯数字")

                if not db_creator.database_exists(db_name):
                    raise ValueError("该数据库不存在")

                tb_name = request.form.get('tb_name').strip()

                if not tb_name:
                    raise ValueError("表名称不能为空")
                if tb_name.isdigit():
                    raise ValueError("表名不能为纯数字")

                if not db_creator.table_exists(db_name, tb_name):
                    raise ValueError("该表不存在")

                if db_creator.drop_table(db_name, tb_name):
                    db_creator.disconnect()  # 断开连接
                    return jsonify({"status": "success",
                                    "message": f"表格 {tb_name} 已成功删除"})
                else:
                    raise ValueError(f"删除表 {tb_name} 失败")
            else:
                raise ValueError("无法连接到SQL服务器")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # 处理GET请求，展示删除数据库的页面
    return render_template('delete_tb.html')  # 应该渲染专门的删除页面

@app.route('/view_db', methods=['GET', 'POST'])
def view_db():
    if request.method == 'POST':
        try:
            # 创建数据库操作实例
            db_creator = MySQLDatabase(**db_config)
            if db_creator.connect():
                db_list = db_creator.list_db(True)
                return jsonify({"databases": db_list})
            else:
                raise ValueError("无法连接到SQL服务器")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template('view_db.html')




@app.route('/view_tb', methods=['GET', 'POST'])
def view_tb():
    if request.method == 'POST':
        try:
            # 创建数据库操作实例
            db_creator = MySQLDatabase(**db_config)

            # 连接到数据库服务器（不指定具体数据库）
            if db_creator.connect():
                # 从表单获取要删除的数据库名称
                db_name = request.form.get('db_name').strip()

                # 验证数据库名称
                if not db_name:
                    raise ValueError("数据库名称不能为空")
                if db_name.isdigit():
                    raise ValueError("数据库名不能为纯数字")

                if not db_creator.database_exists(db_name):
                    print("该数据库不存在")
                    raise ValueError("该数据库不存在")

                tb_list = db_creator.list_tb(db_name)

                return jsonify({"tables": tb_list})
            else:
                raise ValueError("无法连接到SQL服务器")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # 处理GET请求，展示删除数据库的页面
    return render_template('view_tb.html')

@app.route('/download_csv', methods=['GET'])
def download_csv():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 监听所有可用网络接口