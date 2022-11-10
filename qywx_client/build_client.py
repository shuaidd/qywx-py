from .api import *


class Client:
    def __init__(self, **kwargs):
        clt = HttpClient(**kwargs)
        self.userApi = User(clt)
        self.tagApi = UserTag(clt)
        self.departmentApi = Department(clt)
        self.messageApi = Message(clt)
