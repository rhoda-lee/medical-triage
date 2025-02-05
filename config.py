from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
database_username = os.getenv("DB_USERNAME")
database_password = os.getenv("DB_PASSWORD")
database_name = os.getenv('DB_NAME')

print(database_username, database_password, database_name)

connection_str = f'mysql+mysqlconnector://{database_username}:{database_password}@localhost/{database_name}'

engine = create_engine(connection_str)

try:
    connection = engine.connect()
    print('Located and connected to database')
    connection.close()
except Exception as e:
    print(f'An error occured: {e}')

DBSession = sessionmaker(bind = engine)
session = DBSession()
