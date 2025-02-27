from src.models.settings.connection import db_connection_handler
from src.models.entities.users import Users
from sqlalchemy.orm.exc import NoResultFound

class UsersRepository:
    def find_all(self) -> list[Users]:
        try:
            with db_connection_handler as database:
                users = (
                    database.session
                    .query(Users)
                    .all()
                )
                
                return users
        except NoResultFound:
            return []