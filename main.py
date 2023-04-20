from dotenv import load_dotenv
from data_transfer_service import DataTransferService, load_database_from_env

def main():
    load_dotenv()

    prod_db = load_database_from_env("PROD")
    dev_db = load_database_from_env("DEV")

    table_name = input("Digite o nome da tabela: ")

    data_transfer_service = DataTransferService(prod_db, dev_db)
    data_transfer_service.transfer_table(table_name)

    prod_db.close()
    dev_db.close()

if __name__ == "__main__":
    main()
