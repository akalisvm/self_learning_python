"""urllib提供了一系列用于操作URL的功能。"""
import json
from urllib import request

'''
Get
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
例如，对b站自己账号的url：https://space.bilibili.com/11508358/dynamic进行抓取，并返回响应：
'''

path = 'https://space.bilibili.com/11508358/dynamic'
with request.urlopen(path) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))

print('\n')
req = request.Request(path)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, '
                             'like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:', f.read().decode('utf-8'))


def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))

URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
assert data['answer'] == 'yes'
print('ok')
