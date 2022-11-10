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

    def getSimpleUserList(self, appname, department_id):
        return self.client.httpGet(appname, '/user/simplelist', {"department_id": department_id})

    def getDetailUserList(self, appname, department_id):
        return self.client.httpGet(appname, '/user/list', {"department_id": department_id})

    def usrId2openId(self, appname, data):
        return self.client.httpPost(appname, '/user/convert_to_openid', data)

    def openId2usrId(self, appname, data):
        return self.client.httpPost(appname, '/user/convert_to_userid', data)

    def authSuccess(self, appname, user_id):
        return self.client.httpGet(appname, '/user/authsucc', {"userid": user_id})

    def batchInvite(self, appname, data):
        return self.client.httpPost(appname, '/batch/invite', data)

    def getInviteQrCode(self, appname, size_type=1):
        return self.client.httpGet(appname, '/corp/get_join_qrcode', {"size_type": size_type})

    def getUserIdByTelephone(self, appname, data):
        return self.client.httpPost(appname, '/user/getuserid', data)

    def getUserIdByEmail(self, appname, data):
        return self.client.httpPost(appname, '/user/get_userid_by_email', data)

    def getUserIdList(self, appname, data):
        return self.client.httpPost(appname, '/user/list_id', data)


class Department:

    def __init__(self, client: HttpClient):
        self.client = client

    def createDepartment(self, appname, data):
        return self.client.httpPost(appname, '/department/create', data)

    def updateDepartment(self, appname, data):
        return self.client.httpPost(appname, '/department/update', data)

    def deleteDepartment(self, appname, dept_id=None):
        return self.client.httpGet(appname, '/department/delete', {"id": dept_id})

    def getDepartments(self, appname, dept_id=None):
        return self.client.httpGet(appname, '/department/list', {"id": dept_id})

    def getSimpleDepartments(self, appname, dept_id=None):
        return self.client.httpGet(appname, '/department/simplelist', {"id": dept_id})

    def getDepartmentDetail(self, appname, dept_id=None):
        return self.client.httpGet(appname, '/department/simplelist', {"id": dept_id})


class UserTag:

    def __init__(self, client: HttpClient):
        self.client = client

    def createTag(self, appname, data):
        return self.client.httpPost(appname, '/tag/create', data)

    def updateTag(self, appname, data):
        return self.client.httpPost(appname, '/tag/update', data)

    def deleteTag(self, appname, tag_id):
        return self.client.httpGet(appname, '/tag/delete', {"tagid": tag_id})

    def getTagUsers(self,appname, tag_id):
        return self.client.httpGet(appname, '/tag/get', {"tagid": tag_id})

    def addTagUser(self, appname, data):
        return self.client.httpPost(appname, '/tag/addtagusers', data)

    def delTagUser(self, appname, data):
        return self.client.httpPost(appname, '/tag/deltagusers', data)

    def getTagList(self, appname):
        return self.client.httpGet(appname, '/tag/list')

