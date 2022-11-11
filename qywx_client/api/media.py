"""
素材管理
"""

from requests_toolbelt.downloadutils import stream
from requests_toolbelt.multipart.encoder import MultipartEncoder

from ..client.http_client import HttpClient


class Media(object):

    def __init__(self, client: HttpClient):
        self.client = client

    def uploadMedia(self, appname, file_type="file", file_path=None):
        if file_path is None:
            raise ValueError("文件绝对路径不能为空")

        f = open(file_path, 'rb')
        form_data = MultipartEncoder(
            fields={'media': (f.name, f, 'text/plain')}
        )
        return self.client.httpFormDataPost(appname, '/media/upload', form_data, params={"type": file_type})

    def downloadMedia(self, appname, media_id, file_path=None):
        resp = self.client.httpGet(appname, '/media/get', params={'media_id': media_id}, stream=True)

        with open(file_path, 'wb') as fd:
            filename = stream.stream_response_to_file(resp, path=fd)

        print('{0} saved to {1}'.format(media_id, filename))

    def uploadImage(self, appname, file_path=None):
        """
        上传图片
        :param appname:
        :param file_path:
        :return:
        """
        if file_path is None:
            raise ValueError("文件绝对路径不能为空")

        f = open(file_path, 'rb')
        form_data = MultipartEncoder(
            fields={'media': (f.name, f, 'image/png')}
        )
        return self.client.httpFormDataPost(appname, '/media/uploadimg', form_data)
