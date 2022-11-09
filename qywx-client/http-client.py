import requests


class HttpClient:
    def __init__(self, applications):
        self.applications = applications

    def getAppSecret(self, appname=""):
        return self.applications[appname]

    def getAccessToken(self, app_secret=""):
        return ""

    def httpPost(self, url="", appname=""):
        """
        发送post请求
        :param appname: 企业微信应用名称
        :param url: 企业微信接口地址
        :return: 接口响应数据
        """
        secret = self.getAppSecret(appname)
        access_token = self.getAccessToken(secret)
        response = requests.get(url, params={"access_token": access_token})
        return response.json()


client = HttpClient([])
client.httpPost("", "")
