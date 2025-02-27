from src.models.repository.users_repository import UsersRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError

class UsersHandler:
    def __init__(self) -> None:
        self.__users_repository = UsersRepository()

    def find_all(self) -> HttpResponse:
        users = self.__users_repository.find_all()

        if not users:
            raise HttpNotFoundError("No users found")
        
        users_dict = [user.to_dict() for user in users]
        
        return HttpResponse(body={"users": users_dict}, status_code=200)