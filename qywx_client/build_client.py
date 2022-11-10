from .client.http_client import HttpClient
from .api import *


class Client:
    def __init__(self, **kwargs):
        clt = HttpClient(**kwargs)
        self.userApi = User(clt)
