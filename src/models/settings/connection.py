import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DBConnectionHandler:
    def __init__(self) -> None:
        db_user = os.getenv("DB_USER", "default_user")
        db_password = os.getenv("DB_PASSWORD", "default_password")
        db_host = os.getenv("DB_HOST", "localhost")
        db_name = os.getenv("DB_NAME", "default_db")
        self.__connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
        self.__engine = create_engine(self.__connection_string)
        self.Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

    def connect_to_db(self):
        self.session = self.Session()

    def __enter__(self):
        self.connect_to_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = __DBConnectionHandler()