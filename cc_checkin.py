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
    url = 'https://www.cordc.net/user/checkin'
    s = json.dumps({})
    session = requests.session()
    response = requests.post(url, data=s, headers=headers)

    unicode = response.text
    re = unicode.encode('utf-8').decode('unicode_escape')
    msg.append(re)
    
    return msg

if __name__ == "__main__":
    # cookie = os.getenv("cc_cookie")
    cookie = "_ga=GA1.1.656736821.1709306419; uid=57729; email=bluecitizens%40163.com; key=83f78f2b1bcced496526637ea0de6e286bcaf2a396e1a; ip=cc7911a78e7fcdd5965de747ff4238c7; expire_in=1712634482; _ga_WDQMPH0H2X=GS1.1.1712548079.6.1.1712548084.55.0.0; crisp-client%2Fsession%2Ff24e0785-07d5-4a5f-961b-bde1c9b6245b=session_b037b4aa-e2bd-4b00-a01f-4a0d6e208f12"
    push(sign(cookie))