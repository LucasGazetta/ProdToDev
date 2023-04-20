# Data Transfer Tool
A command-line tool for transferring table data from a production SQL Server database to a development SQL Server database, ensuring that only non-duplicate rows are inserted into the development database.

# Requirements
Python 3.8 or later
pyodbc library for connecting to SQL Server
python-dotenv library for handling environment variables
You can install the required libraries using pip:

-- pip install pyodbc python-dotenv

# Setup
1. Clone this repository and navigate to the project directory.
2. Create a .env file in the project directory and provide the necessary database connection information for both production and development databases:

PROD_DRIVER={SQL Server driver}

PROD_HOST={Production database host}

PROD_USER={Production database username}

PROD_PASSWORD={Production database password}

PROD_DATABASE={Production database name}


DEV_DRIVER={SQL Server driver}

DEV_HOST={Development database host}

DEV_USER={Development database username}

DEV_PASSWORD={Development database password}

DEV_DATABASE={Development database name}

Replace the placeholders with your actual database connection details.

# Usage
To run the data transfer tool, execute the following command:
python main.py

The tool will prompt you to enter the name of the table you wish to transfer. After you enter the table name, the tool will transfer all columns of the specified table from the production database to the development database, inserting only the data that is not already present in the development database.

# Project Structure
The project consists of the following files:

* main.py: The main script that prompts the user for input and initiates the data transfer process.
* database.py: Contains the Database class for connecting to SQL Server and handling data fetching and insertion.
* data_transfer_service.py: Contains the DataTransferService class responsible for transferring data between the production and development databases.

# Testing
The project includes unit tests for individual components of the data transfer tool. To run the tests, execute the following command:

-- python test_data_transfer.py  
