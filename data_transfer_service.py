from database import Database
import os

class DataTransferService:
    def __init__(self, prod_db: Database, dev_db: Database):
        self.prod_db = prod_db
        self.dev_db = dev_db

    def transfer_data(self, tables_with_columns):
        for table_name, columns in tables_with_columns.items():
            data = self.prod_db.fetch_data(table_name, columns)
            self.dev_db.insert_data(table_name, columns, data)

    def transfer_table(self, table_name):
        columns = self.prod_db.fetch_column_names(table_name)
        dev_data = self.dev_db.fetch_data(table_name, columns)
        data_to_transfer = self.prod_db.fetch_data_not_in_dev(table_name, columns, dev_data)
        self.dev_db.insert_data(table_name, columns, data_to_transfer)

def load_database_from_env(prefix):
    driver = os.getenv(f"{prefix}_DRIVER")
    host = os.getenv(f"{prefix}_HOST")
    user = os.getenv(f"{prefix}_USER")
    password = os.getenv(f"{prefix}_PASSWORD")
    database = os.getenv(f"{prefix}_DATABASE")

    return Database(driver, host, user, password, database)
