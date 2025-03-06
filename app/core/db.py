import pymysql
from .config import db_host, db_user, db_password, db_name

class DatabaseManager:
    def __init__(self):
        self.connection = None

    def create_connection(self):
        try:
            self.connection = pymysql.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            print(f"数据库连接错误: {e}")
            return None
        return self.connection

    def fetch_query(self, query, params=None):
        if not self.connection or not self.connection.open:
            self.create_connection()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"查询错误: {e}")
            return None

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.open:
            self.create_connection()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
        except pymysql.MySQLError as e:
            print(f"执行错误: {e}")
            self.connection.rollback()

    def close_connection(self):
        if self.connection and self.connection.open:
            self.connection.close()