from ..client.http_client import HttpClient


class Message(object):

    def __init__(self, client: HttpClient):
        self.client = client

    def send(self, appname, data):
        return self.client.httpPost(appname, '/message/send', data)
