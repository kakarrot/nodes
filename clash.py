from xml.dom.minicompat import NodeList
import requests
import json
import warnings
import base64

import string

import git


# warnings.filterwarnings('ignore')

confUrl = "https://api.buliang0.cf/opconf.json"

proxies = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}

response = requests.get(
    confUrl, 
    proxies = proxies
)

# jsonText = '{"code":200,"msg":"success","data":{"items":[{"id":2,"name":"免费节点(更新时间:15:19:24)","tag":2,"free":true,"items":[{"free":"true","city":"ss:日本-153.4KB/s","ovpn":"c3M6Ly9ZV1Z6TFRJMU5pMW5ZMjA2VkVWNmFtWkJXWEV5U1dwMGRXOVRAODUuMjA4LjEwOC4yMDo2Njc5IyVFNiU5NyVBNSVFNiU5QyVBQy0xNTMuNEtCJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""},{"free":"true","city":"trojan:中国-7.69MB/s","ovpn":"dHJvamFuOi8vYzlhM2E2MWQtNWQ0OS00MTU4LTllNjAtNmZhMzI2ODRiMTIyQGNtLnNwYWNlei5jbG91ZDozMDAwMyMlRTQlQjglQUQlRTUlOUIlQkQtNy42OU1CJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""},{"free":"true","city":"ss:日本-869.9KB/s","ovpn":"c3M6Ly9ZV1Z6TFRJMU5pMW5ZMjA2VW1WNGJrSm5WVGRGVmpWQlJIaEhAODUuMjA4LjEwOC4yMDo3MDAyIyVFNiU5NyVBNSVFNiU5QyVBQy04NjkuOUtCJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""},{"free":"true","city":"trojan:中国-13.34MB/s","ovpn":"dHJvamFuOi8vNjNlYzc1NmQtMWY2YS0zNmM4LWE5ZmQtMDI1ZjRhY2ZjNzRmQGhuLnpmbm9kZS5vcmc6MzAyMTcjJUU0JUI4JUFEJUU1JTlCJUJELTEzLjM0TUIlMkZzJTI4WW91dHViZSUzQSVFNCVCOCU4RCVFOCU4OSVBRiVFNiU5RSU5NyUyOQ==","icon":""},{"free":"true","city":"ss:美国-1.70MB/s","ovpn":"c3M6Ly9ZV1Z6TFRJMU5pMW5ZMjA2Wm1GQ1FXOUVOVFJyT0RkVlNrYzNAMzguMTIxLjQzLjY1OjIzNzUjJUU3JUJFJThFJUU1JTlCJUJELTEuNzBNQiUyRnMlMjhZb3V0dWJlJTNBJUU0JUI4JThEJUU4JTg5JUFGJUU2JTlFJTk3JTI5","icon":""},{"free":"true","city":"ss:日本-167.9KB/s","ovpn":"c3M6Ly9ZV1Z6TFRJMU5pMW5ZMjA2VkVWNmFtWkJXWEV5U1dwMGRXOVRAODUuMjA4LjEwOC4yMDo2Njk3IyVFNiU5NyVBNSVFNiU5QyVBQy0xNjcuOUtCJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""},{"free":"true","city":"trojan:德国-295.0KB/s","ovpn":"dHJvamFuOi8vZGZiZjBkNjctZjAzZC00MTg0LWEyMjQtYzJkNjRhNTcxZjk5QHM0Lmhhenoud2luOjEyMzQwIyVFNSVCRSVCNyVFNSU5QiVCRC0yOTUuMEtCJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""},{"free":"true","city":"trojan:新加坡-2.02MB/s","ovpn":"dHJvamFuOi8vZGZiZjBkNjctZjAzZC00MTg0LWEyMjQtYzJkNjRhNTcxZjk5QHMyLmhhenoud2luOjEyMzQwIyVFNiU5NiVCMCVFNSU4QSVBMCVFNSU5RCVBMS0yLjAyTUIlMkZzJTI4WW91dHViZSUzQSVFNCVCOCU4RCVFOCU4OSVBRiVFNiU5RSU5NyUyOQ==","icon":""},{"free":"true","city":"trojan:美国-340.8KB/s","ovpn":"dHJvamFuOi8vZGZiZjBkNjctZjAzZC00MTg0LWEyMjQtYzJkNjRhNTcxZjk5QHMzLmhhenoud2luOjEyMzQwIyVFNyVCRSU4RSVFNSU5QiVCRC0zNDAuOEtCJTJGcyUyOFlvdXR1YmUlM0ElRTQlQjglOEQlRTglODklQUYlRTYlOUUlOTclMjk=","icon":""}]}]}}';
# response = json.loads(jsonText, strict = False)


list = response.json().get("data").get("items")[0].get("items")

subscribe = ""

for item in list:
    ovpnItem = item.get("ovpn")
    ovpn = base64.b64decode(ovpnItem)
    ovpn = str(ovpn,'utf8')
    # text = unquote(ovpn, 'utf-8')
    # text = quote(text, 'utf-8')
    subscribe += ovpn + "|"

subscribe = subscribe.strip('|')
print(subscribe)

# 写入cyou文件，并且commit到git
repo = git.Repo(path='.')

with open('ovpn', 'w') as fobj:
    fobj.write(subscribe)
repo.git.add(all=True)
repo.index.commit('update ovpn content')

repo.remote().push()