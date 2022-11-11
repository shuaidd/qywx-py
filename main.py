import qywx_client

if __name__ == '__main__':
    client = qywx_client.Client(applications={
        "address-book": {
            "appName": "address-book",
            "appSecret": "AfjvAed_ulqhK0OqTprDQ6xOSnqaT34ll2LsRe0D2NA"
        }
    }, corp_id="ww36e0a51aab349a7d", timeout=5000, use_redis=True)

    # res = client.mediaApi.uploadMedia('address-book',
    #                                   file_path='/Users/ddshuai/soft-install/workspace/github/qywx-py/pyproject.toml')
    # print(res)

    # client.mediaApi.downloadMedia("address-book",
    #                               media_id='3aNHzgFJKe2BArBHygdhH3ZJjzB8vFqATWCr5dysEns8x4HKALukn1MNTuy9biVI9',
    #                               file_path='/Users/ddshuai/soft-install/workspace/github/qywx-py/pyproject-dw.toml')

    res = client.mediaApi.uploadImage("address-book",
                                      file_path='/Users/ddshuai/Downloads/WechatIMG16.png')
    print(res)
