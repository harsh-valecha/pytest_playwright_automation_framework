import sqlite3

class DBUtils:

    @staticmethod
    def connect_to_db(db_path):
        conn = sqlite3.connect(db_path)
        return conn

    @staticmethod
    def fetch_data(query, db_path='data/test.db'):
        conn = DBUtils.connect_to_db(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
