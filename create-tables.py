from sqlalchemy import create_engine
from src.models.entities.users import Base
import os

db_user = os.getenv("DB_USER", "sa")
db_password = os.getenv("DB_PASSWORD", "StrongPassword123")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "users")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

print(connection_string)

engine = create_engine(connection_string)

# Dropar todas as tabelas existentes (opcional, use com cuidado)
Base.metadata.drop_all(engine)

# Criar todas as tabelas
Base.metadata.create_all(engine)

print("Tabelas criadas com sucesso")