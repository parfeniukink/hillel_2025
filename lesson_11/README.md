# HTTP

- path (https://pokeapi.co/api/v2/pokemon/77)
- method
    - GET - claim something
    - POST - add something
    - PUT - change something
    - PATCH - change something
    - DELETE - delete something
- payload
    - query params
    - body



HTTP GET https://pokeapi.co/api/v2/pokemon?id=77
HTTP POST https://pokeapi.co/api/v2/pokemon
{
    "id": 77
}


Client -> Browser -> HTTP Request -> Nginx -> WSGI / ASGI Server -> `requests.Request`

-> business logic -> `Response` -> Application Server (WSGI/ASGI) -> Nginx -> Browser -> Client


requests.Request
    - query_params
    - body
