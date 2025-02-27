from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.entities.users import Base
import os

db_user = os.getenv("DB_USER", "default_user")
db_password = os.getenv("DB_PASSWORD", "default_password")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "default_db")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(connection_string)

# Criar todas as tabelas
Base.metadata.create_all(engine)

print("Tabelas criadas com sucesso")