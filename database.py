import pyodbc

class Database:
    def __init__(self, driver, host, user, password, database):
        self.connection = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"SERVER={host};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password}"
        )

    def fetch_data(self, table_name, columns):
        columns_str = ', '.join(columns)
        sql = f"SELECT {columns_str} FROM {table_name}"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def insert_data(self, table_name, columns, data):
        cursor = self.connection.cursor()
        for row in data:
            columns_str = ', '.join(columns)
            values_str = ', '.join([f"'{row[col]}'" for col in columns])
            sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
            cursor.execute(sql)
        self.connection.commit()

    def fetch_column_names(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        columns = [column[0] for column in cursor.description]
        return columns

    def fetch_data_not_in_dev(self, table_name, columns, dev_data):
        columns_str = ', '.join(columns)
        dev_data_str = ', '.join([f"({', '.join(map(str, row))})" for row in dev_data])
        sql = f"SELECT {columns_str} FROM {table_name} WHERE ({columns_str}) NOT IN ({dev_data_str})"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
