from src.models.repository.users_repository import UsersRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from sqlalchemy.exc import IntegrityError

class UsersHandler:
    def __init__(self) -> None:
        self.__users_repository = UsersRepository()

    def find_all(self) -> HttpResponse:
        users = self.__users_repository.find_all()

        if not users:
            raise HttpNotFoundError("No users found")
        
        users_dict = [user.to_dict() for user in users]
        
        return HttpResponse(body={"users": users_dict}, status_code=200)

    def create_user(self, request: HttpRequest) -> HttpResponse:
        try:
            user_data = request.body
            new_user = self.__users_repository.create_user(user_data)
            return HttpResponse(body=new_user.to_dict(), status_code=201)
        except KeyError as e:
            return HttpResponse(body={"error": f"Missing field: {str(e)}"}, status_code=400)
        except IntegrityError as e:
            return HttpResponse(body={"error": str(e)}, status_code=409)
        except Exception as e:
            return HttpResponse(body={"error": str(e)}, status_code=400)
    
    def delete_user(self, user_id: int) -> HttpResponse:
        try:
            deleted = self.__users_repository.delete_user(user_id)
            if not deleted:
                raise HttpNotFoundError(f"User with id {user_id} not found")
            return HttpResponse(body={"message": "User deleted successfully"}, status_code=200)
        except Exception as e:
            return HttpResponse(body={"error": str(e)}, status_code=400)