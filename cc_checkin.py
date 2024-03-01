import json
import os

import requests
import urllib3

# 推送PLUS的token
Token = 'AXu-8g4P52sv9zs'

def push(content):
    print(content)
    if Token != '':
        url = "http://103.82.54.214:8004/message?token={}".format(Token)
        headers = {'Content-Type': 'application/json'}
        data = {
            'title': 'CordCloud 签到',
            'message': content,
            'priority': '0'

        }
        requests.post(url, data)
    else:
        print('未使用消息推送推送！')

urllib3.disable_warnings()

def sign(cookie):
    msg = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
        "Cookie": cookie,
    }
    url = 'https://www.c-cloud.xyz/user/checkin'
    s = json.dumps({})
    session = requests.session()
    response = requests.post(url, data=s, headers=headers)

    unicode = response.text
    re = unicode.encode('utf-8').decode('unicode_escape')
    msg.append(re)
    
    return msg

if __name__ == "__main__":
    cookie = os.getenv("cc_cookie")
    push(sign(cookie))