from lib.httpx_client import HttpxClient


def get_http_client() -> HttpxClient:
    return HttpxClient(
        base_url="https://api.example.com",
        headers={"Authorization": "Bearer <token>"},
        timeout=10.0,
        verify=True,
        mode="sync",
    )