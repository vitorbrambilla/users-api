from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.users import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class UsersRepository:
    def find_all(self) -> List[Users]:
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

    def create_user(self, user_info: Dict) -> Users:
        with db_connection_handler as database:
            try:
                # Verificar se o email já existe
                existing_user = (
                    database.session
                    .query(Users)
                    .filter(Users.email == user_info.get("email"))
                    .first()
                )
                if existing_user:
                    raise Exception("E-mail em uso")

                new_user = Users(
                    name=user_info.get("name"),
                    email=user_info.get("email"),
                    phone=user_info.get("phone"),
                    status=user_info.get("status")
                )
                database.session.add(new_user)
                database.session.commit()
                database.session.refresh(new_user)
                return new_user
          
            except Exception as e:
                database.session.rollback()
                raise e
            
    def update_user(self, user_id: int, user_info: Dict) -> Users:
        with db_connection_handler as database:
            try:
                user = (
                    database.session
                    .query(Users)
                    .filter(Users.id == user_id)
                    .first()
                )
                if not user:
                    return None

                user.name = user_info.get("name", user.name)
                user.email = user_info.get("email", user.email)
                user.phone = user_info.get("phone", user.phone)
                user.status = user_info.get("status", user.status)

                database.session.commit()
                database.session.refresh(user)
                return user
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete_user(self, user_id: int) -> bool:
        with db_connection_handler as database:
            try:
                user = (
                    database.session
                    .query(Users)
                    .filter(Users.id == user_id)
                    .first()
                )
                if not user:
                    return False
                database.session.delete(user)
                database.session.commit()
                return True
            except Exception as e:
                database.session.rollback()
                raise e