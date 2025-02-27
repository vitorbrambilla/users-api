from sqlalchemy import create_engine
import os

db_user = os.getenv("DB_USER", "default_user")
db_password = os.getenv("DB_PASSWORD", "default_password")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "default_db")

print(db_user, db_password, db_host, db_name)

connection_string = f"postgresql://{db_user}:StrongPassword123@{db_host}:5432/{db_name}"

print(connection_string)

try:
    engine = create_engine(connection_string)
    connection = engine.connect()
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")