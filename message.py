import requests

content = requests.get('https://www.baidu.com')
content.encoding = 'utf-8'
print(content.text)
print(content.encoding)
