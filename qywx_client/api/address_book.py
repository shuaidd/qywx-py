"""
通讯录管理
"""
from ..client.http_client import HttpClient


class User:

    def __init__(self, client: HttpClient):
        self.client = client

    def createUser(self, appname=None, data=None):
        return self.client.httpPost(appname, '/user/create', data)

    def updateUser(self, appname=None, data=None):
        return self.client.httpPost(appname, '/user/update', data)

    def getUser(self, appname, user_id):
        return self.client.httpGet(appname, '/user/get', {"userid": user_id})

    def deleteUser(self, appname, user_id):
        return self.client.httpGet(appname, '/user/delete', {"userid": user_id})

    def batchDeleteUser(self, appname, data):
        return self.client.httpPost(appname, '/user/batchdelete', data)
