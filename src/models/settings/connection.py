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
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        if self.__engine is None:
            self.connect_to_db()
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = __DBConnectionHandler()