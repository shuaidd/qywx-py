import requests
import redis


class HttpClientConfig:

    def __init__(self, corp_id,
                 baseurl="https://qyapi.weixin.qq.com/cgi-bin",
                 timeout=50000,
                 applications=None,
                 use_redis=False,
                 redis_url='localhost',
                 redis_port=6379,
                 username=None,
                 password=None
                 ):
        self.password = password
        self.username = username
        self.redis_port = redis_port
        self.redis_url = redis_url
        self.baseUrl = baseurl
        self.applications = applications or {}
        self.useRedis = use_redis
        self.corpId = corp_id
        self.timeout = timeout

        if use_redis:
            self.redis_client = redis.Redis(host=redis_url, port=redis_port, db=0, username=username, password=password)

    def __str__(self):
        fmt = 'baseUrl: {baseUrl} applications: {applications}, corpId={corpId}, useRedis={useRedis}'.format(
            baseUrl=self.baseUrl,
            applications=self.applications,
            corpId=self.corpId,
            useRedis=self.useRedis
        )
        return fmt


class HttpClient(HttpClientConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('客户端配置信息--->', self)

    def getAppSecret(self, appname=""):
        if appname:
            app = self.applications.get(appname)
            if app:
                return app['appSecret']
        return ""

    def getAccessToken(self, appname=None):
        app_secret = self.getAppSecret(appname)
        if not app_secret:
            raise Exception('无法获取app_secret')
        redis_key = f'qywx_py_access_token_{appname}'.format(appname=appname)
        if self.useRedis:
            access_token = self.redis_client.get(redis_key)
            if access_token:
                print("从redis缓存获取access_token  {access_token}".format(access_token=access_token))
                return access_token

        response = requests.get('{baseUrl}/gettoken'.format(baseUrl=self.baseUrl), params={
            "corpid": self.corpId,
            "corpsecret": app_secret
        })

        data = response.json()

        if data['errcode'] == 0:
            if self.useRedis:
                self.redis_client.set(redis_key, response.json()['access_token'], ex=7200)
            return data['access_token']

        raise Exception('获取access_token失败-->', data['errcode'], data['errmsg'])

    def httpPost(self, appname="", uri="", data=None):
        """
        发送post请求
        :param data: 请求的数据
        :param uri: 企业微信接口地址
        :param appname: 企业微信应用名称
        :return: 接口响应数据
        """
        access_token = self.getAccessToken(appname)
        response = requests.post(self.baseUrl + uri, params={"access_token": access_token, "debug": 1},
                                 json=data)

        return_val = response.json()
        if return_val['errcode'] == 0:
            return return_val

        raise Exception('企业微信接口调用失败-->', return_val['errcode'], return_val['errmsg'])

    def httpFormDataPost(self, appname, uri, form_data, params=None):
        access_token = self.getAccessToken(appname)

        if params is None:
            params = {}

        params['access_token'] = access_token
        params['debug'] = 1
        response = requests.post(self.baseUrl + uri, params=params,
                                 data=form_data, headers={'Content-Type': 'multipart/form-data'})

        return_val = response.json()
        if return_val['errcode'] == 0:
            return return_val

        raise Exception('企业微信接口调用失败-->', return_val['errcode'], return_val['errmsg'])

    def httpGet(self, appname="", uri="", params=None, stream=None):
        """
        发送get请求
        :param stream:
        :param appname: 企业微信应用名称
        :param uri: 企业微信接口地址
        :param params: 参数
        :return: 接口响应数据
        """
        if params is None:
            params = {}
        access_token = self.getAccessToken(appname)
        params['access_token'] = access_token
        params['debug'] = 1
        response = requests.get(self.baseUrl + uri, params=params, stream=stream)

        if stream:
            return response

        return_val = response.json()
        if return_val['errcode'] == 0:
            return return_val

        raise Exception('企业微信接口调用失败-->', return_val['errcode'], return_val['errmsg'])
