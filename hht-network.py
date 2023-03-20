#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @time: 2022/9/9 7:46 AM
import urllib.parse
import urllib.request
import json

url = 'http://10.10.16.12/api/portal/v1/login'

payload = {
    'domain': 'telecom',
    'username': 'ffffff',
    'password': 'ffffff'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers=headers)

with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')
    reply = json.loads(content)

if reply['reply_code'] == 0:
    print('登录成功')
else:
    print('登录失败：', reply['reply_msg'])