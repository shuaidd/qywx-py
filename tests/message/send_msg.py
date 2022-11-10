import qywx_client

if __name__ == '__main__':
    client = qywx_client.Client(applications={
        "report": {
            "appName": "report",
            "appSecret": "QjsfcXZSM1R82nm8nMnWzvWgElTJRbl1I2B0FFRBliw",
            "agentId": 1000009
        }
    }, corp_id="ww36e0a51aab349a7d", timeout=5000, use_redis=True)

    res = client.messageApi.send("report", {
        "touser": "20170410022717",
        "msgtype": "text",
        "agentid": 1000009,
        "text": {
            "content": "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
        },
        "safe": 0
    })
    print(res)
