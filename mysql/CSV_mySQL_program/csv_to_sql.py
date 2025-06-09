from flask import Flask, render_template, request, jsonify

import os

from werkzeug.utils import secure_filename
import csv
import mysql.connector
from mysql.connector import Error  #与 MySQL 数据库交互过程出现的错误
from flask import make_response
import csv
import pandas as pd


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
        """获取指定数据库中所有表的列表（排除系统数据库）"""
        if not self.connection or not self.connection.is_connected():
            self.logger.error("未连接到数据库服务器")
            return []

        # 定义系统数据库列表
        SYSTEM_DATABASES = {'sakila', 'world', 'sys', 'information_schema', 'performance_schema', 'mysql'}

        # 安全检查：防止操作系统数据库
        if db_name.lower() in SYSTEM_DATABASES:
            raise ValueError(f'拒绝操作系统数据库: {db_name}')

        try:
            with self.connection.cursor() as cursor:
                # 查询指定数据库中的所有表
                query = """
                        SELECT TABLE_NAME
                        FROM information_schema.tables
                        WHERE TABLE_SCHEMA = %s \
                        """
                cursor.execute(query, (db_name,))
                return [row[0] for row in cursor.fetchall()]

        except self.connection.Error as e:  # 捕获数据库特定异常
            self.logger.error(f"获取表列表时发生错误: {e}")
            return []

    def show_table(self, db_name, tb_name, limit=1000):
        """
        执行 SELECT * FROM db_name.tb_name 查询，返回表数据（带表头）
        :param db_name: 数据库名称
        :param tb_name: 表名称
        :param limit: 限制返回的行数（默认1000行）
        :return: 包含表头和数据的列表，失败返回 None
        """
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return None

        # 定义系统数据库列表
        SYSTEM_DATABASES = {'sakila', 'world', 'sys', 'information_schema', 'performance_schema', 'mysql'}

        # 安全检查：拒绝操作系统数据库
        if db_name.lower() in SYSTEM_DATABASES:
            print(f"拒绝操作：系统数据库 {db_name} 不可访问")
            return None

        try:
            # 切换到目标数据库
            if not self.use_database(db_name):
                print(f"无法切换到数据库：{db_name}")
                return None

            # 构建安全的表名（使用反引号转义，防止 SQL 注入）
            tb_name_safe = f"`{tb_name}`"

            # 构建查询语句（带 LIMIT 分页）
            query = f"SELECT * FROM {tb_name_safe} LIMIT {limit}"

            cursor = self.connection.cursor()
            cursor.execute(query)

            # 获取表头（列名）
            columns = [column[0] for column in cursor.description]

            # 获取所有数据行
            rows = cursor.fetchall()

            # 组装结果：[表头, 数据行列表]
            result = [columns] + [list(row) for row in rows]
            print(f"成功查询表 {db_name}.{tb_name}，返回 {len(rows)} 条记录")
            return result

        except self.connection.Error as e:
            print(f"查询表数据时发生错误：{e}")
            return None

        finally:
            if cursor:
                cursor.close()

    def download_csv(self, db_name, tb_name, output_path, limit=10000):
        """
        从指定表导出数据到CSV文件（带表头）
        :param db_name: 数据库名
        :param tb_name: 表名
        :param output_path: CSV文件保存路径
        :param limit: 最大导出行数（默认10000行）
        :return: 成功/失败
        """
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库服务器")
            return False

        # 安全检查：拒绝操作系统数据库
        if db_name.lower() in {'sakila', 'world', 'sys', 'information_schema', 'performance_schema', 'mysql'}:
            print(f"拒绝操作：系统数据库 {db_name} 不可访问")
            return False

        try:
            # 切换到目标数据库
            if not self.use_database(db_name):
                print(f"无法切换到数据库：{db_name}")
                return False

            # 构建安全的表名（使用反引号转义，防止 SQL 注入）
            tb_name_safe = f"`{tb_name}`"

            # 构建查询语句（带 LIMIT 分页）
            query = f"SELECT * FROM {tb_name_safe} LIMIT {limit}"

            cursor = self.connection.cursor()
            cursor.execute(query)

            # 获取表头（列名）
            columns = [column[0] for column in cursor.description]

            # 获取所有数据行
            rows = cursor.fetchall()

            # 写入CSV文件
            with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(columns)  # 写入表头
                writer.writerows(rows)  # 写入数据行

            print(f"成功导出表 {db_name}.{tb_name} 到 {output_path}，共导出 {len(rows)} 条记录")
            return True

        except self.connection.Error as e:
            print(f"导出表数据时发生错误：{e}")
            return False

        finally:
            if cursor:
                cursor.close()







def parse_csv_structure(csv_path):
    df = pd.read_csv(csv_path, nrows=100)
    headers = df.columns.tolist()
    column_types = []

    for col in df.columns:
        dtype = df[col].dtype
        if pd.api.types.is_integer_dtype(dtype):
            column_types.append("INT")
        elif pd.api.types.is_float_dtype(dtype):
            column_types.append("DECIMAL(10,2)")
        else:
            column_types.append("VARCHAR(255)")

    return headers, column_types


def get_column_definition(headers, types):
    """
    根据列名和数据类型生成SQL表定义语句

    Args:
        headers (list): 列名列表
        types (list): 数据类型列表

    Returns:
        str: SQL列定义语句
    """
    column_defs = []

    for header, col_type in zip(headers, types):
        # 处理特殊类型映射
        if header.startswith('is') and col_type == 'INT':
            sql_type = 'TINYINT(1)'
        elif col_type == 'DECIMAL(10,2)':
            sql_type = 'DECIMAL(5,2)'  # 调整精度为5,2
        else:
            sql_type = col_type

        # 添加列定义（带NOT NULL约束）
        column_defs.append(f"`{header}` {sql_type} NOT NULL")

    # 合并为完整的SQL语句
    return ",\n".join(column_defs)

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


if not os.path.exists('downloads'):
    os.makedirs('downloads')



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
                headers, column_types = parse_csv_structure(file_path)
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
                            columns_definition = get_column_definition(headers, column_types)



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
                db_creator.disconnect()
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

            try:
                # 连接到数据库服务器
                if not db_creator.connect():
                    raise ValueError("无法连接到SQL服务器")

                # 从表单获取要查看的数据库名称
                db_name = request.form.get('db_name').strip()

                # 验证数据库名称
                if not db_name:
                    raise ValueError("数据库名称不能为空")
                if db_name.isdigit():
                    raise ValueError("数据库名不能为纯数字")

                # 检查数据库是否存在
                if not db_creator.database_exists(db_name):
                    raise ValueError("该数据库不存在")

                # 获取表列表
                tb_list = db_creator.list_tb(db_name)
                return jsonify({"tables": tb_list})

            finally:
                db_creator.disconnect()  # 确保关闭数据库连接

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            app.logger.error(f"查看表列表失败: {str(e)}")
            return jsonify({"error": "服务器内部错误，请稍后重试"}), 500

    # 处理GET请求，展示查看表的页面
    return render_template('view_tb.html')


@app.route('/show_tb', methods=['GET', 'POST'])  # 添加 GET 方法
def show_table():
    if request.method == 'GET':
        # 处理 GET 请求：渲染空表单页面
        return render_template('show_tb.html')

    elif request.method == 'POST':
        try:
            db_name = request.form.get('db_name').strip()
            tb_name = request.form.get('tb_name').strip()

            # 表单验证：检查必填字段
            if not db_name or not tb_name:
                return jsonify({"error": "请填写数据库名和表名"}), 400

            # 创建数据库连接
            db = MySQLDatabase(**db_config)
            if not db.connect():
                return jsonify({"error": "数据库连接失败"}), 500

            # 执行查询
            table_data = db.show_table(db_name, tb_name)
            if not table_data:
                return jsonify({"error": "查询表数据失败：可能表不存在或无权限"}), 400

            # 处理结果：返回前100条数据（避免大数据量）
            headers = table_data[0]
            rows = table_data[1:101]  # 限制返回100条，可根据需求调整

            # 返回 JSON 数据给前端
            return jsonify({
                "success": True,
                "db_name": db_name,
                "tb_name": tb_name,
                "headers": headers,
                "rows": rows,
                "total": len(table_data) - 1  # 总数据量（排除表头）
            })

        except Exception as e:
            app.logger.error(f"查询表数据失败: {str(e)}", exc_info=True)
            return jsonify({
                "error": "数据库或表不存在",
                "details": str(e)  # 开发环境可返回详细信息，生产环境建议移除
            }), 500

        finally:
            if db and db.connection and db.connection.is_connected():
                db.disconnect()


@app.route('/download_tb', methods=['POST'])
def download_table():
    try:
        db_name = request.form.get('db_name').strip()
        tb_name = request.form.get('tb_name').strip()

        # 表单验证
        if not db_name or not tb_name:
            return jsonify({"error": "请填写数据库名和表名"}), 400

        # 创建数据库连接
        db = MySQLDatabase(**db_config)
        if not db.connect():
            return jsonify({"error": "数据库连接失败"}), 500

        # 生成临时CSV文件路径
        download_folder = 'downloads'
        os.makedirs(download_folder, exist_ok=True)
        filename = f"{db_name}_{tb_name}_export.csv"
        output_path = os.path.join(download_folder, filename)

        # 调用download_csv方法导出数据
        if not db.download_csv(db_name, tb_name, output_path):
            return jsonify({"error": "数据导出失败"}), 500

        # 返回CSV文件作为响应
        with open(output_path, 'rb') as f:
            response = make_response(f.read())
            response.headers['Content-Disposition'] = f'attachment; filename={filename}'
            response.headers['Content-Type'] = 'text/csv; charset=utf-8-sig'  # 使用UTF-8 BOM确保Excel正确解析中文

        # 可选：下载后删除临时文件
        os.remove(output_path)

        return response

    except Exception as e:
        app.logger.error(f"下载数据失败: {str(e)}", exc_info=True)
        return jsonify({
            "error": "数据下载失败，请重试",
            "details": str(e)
        }), 500

    finally:
        if db and db.connection and db.connection.is_connected():
            db.disconnect()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 监听所有可用网络接口