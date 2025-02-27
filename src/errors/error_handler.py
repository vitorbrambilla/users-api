from src.http_types.http_response import HttpResponse

def handle_error(error) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Error",
                "details": str(error)
            }]
        }
    )