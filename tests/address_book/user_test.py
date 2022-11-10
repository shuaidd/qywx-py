import qywx_client

if __name__ == '__main__':
    client = qywx_client.Client(applications={
        "address-book": {
            "appName": "address-book",
            "appSecret": "AfjvAed_ulqhK0OqTprDQ6xOSnqaT34ll2LsRe0D2NA"
        }
    }, corp_id="ww36e0a51aab349a7d", timeout=5000, use_redis=True)

    userDetail = client.userApi.getUser("address-book", "20170410022717")
    print(userDetail)
