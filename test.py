import requests
import json
import time
import warnings


import random
import string

import git


# warnings.filterwarnings('ignore')

a = string.ascii_letters + string.digits
key = random.sample(a,8)
password = "".join(key)

millis = int(round(time.time() * 1000))
email = f'{millis}@ppi.com'

data = {
    "email": email,
    "password": password
}

#print(data)

proxies = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}


# response = requests.post(
#     "https://tmyun.cyou/api/v1/passport/auth/register", 
#     data = data, 
#     proxies=proxies, 
#     verify=False
# )

str = '{"data":{"plan_id":5,"token":"e08b9f5e8a0bd69e7c65a18c877c2b65","expired_at":1653641520,"u":0,"d":0,"transfer_enable":1073741824,"email":"mayun3@yeah.net:","plan":{"id":5,"group_id":1,"transfer_enable":1,"name":"\u514d\u8d39\u8bd5\u75282\u5c0f\u65f6","show":0,"sort":1,"renew":0,"content":"\u65b0\u7528\u6237\u8bd5\u7528\u5957\u9910<br>\n\u4ec5\u9650\u4f53\u9a8c\u4e00\u6b21<br>","month_price":null,"quarter_price":null,"half_year_price":null,"year_price":null,"two_year_price":null,"three_year_price":null,"onetime_price":0,"reset_price":999,"reset_traffic_method":2,"created_at":1646616893,"updated_at":1650467300},"subscribe_url":"https:\/\/tmyunsub.xyz\/api\/v1\/client\/subscribe?token=e08b9f5e8a0bd69e7c65a18c877c2b65","reset_day":null}}';
response = json.loads(str, strict = False)


token = response.get("data").get("token")

print("https://tmyunsub.xyz/api/v1/client/subscribe?token=" + token)


subscribe = requests.get("https://tmyunsub.xyz/api/v1/client/subscribe?token=" + token)

print(subscribe.text)

# 写入cyou文件，并且commit到git
repo = git.Repo(path='.')

with open('cyou', 'w') as fobj:
    fobj.write("c3M6Ly9ZMmhoWTJoaE1qQXRhV1YwWmkxd2IyeDVNVE13TlRveFpUbG1aVFZqTmkxbE16UXpMVFJtWTJRdFltSXhOaTFpWTJJMVlqUXlOamRsWXpNQHgudG15dW5zdWIueHl6OjM4MDExIyVFOSVBNiU5OSVFNiVCOCVBRiUyMCU3QyUyMElFUEwlRTQlQjglOTMlRTclQkElQkYNCnNzOi8vWTJoaFkyaGhNakF0YVdWMFppMXdiMng1TVRNd05Ub3haVGxtWlRWak5pMWxNelF6TFRSbVkyUXRZbUl4TmkxaVkySTFZalF5TmpkbFl6TUB4LnRteXVuc3ViLnh5ejozODAxMiMlRTklQTYlOTklRTYlQjglQUYyJTIwJTdDJTIwSUVQTCVFNCVCOCU5MyVFNyVCQSVCRg0Kc3M6Ly9ZMmhoWTJoaE1qQXRhV1YwWmkxd2IyeDVNVE13TlRveFpUbG1aVFZqTmkxbE16UXpMVFJtWTJRdFltSXhOaTFpWTJJMVlqUXlOamRsWXpNQHgyLnRteXVuc3ViLnh5ejozODAxMyMlRTklQTYlOTklRTYlQjglQUYzJTIwJTdDJTIwSUVQTCVFNCVCOCU5MyVFNyVCQSVCRg0Kc3M6Ly9ZMmhoWTJoaE1qQXRhV1YwWmkxd2IyeDVNVE13TlRveFpUbG1aVFZqTmkxbE16UXpMVFJtWTJRdFltSXhOaTFpWTJJMVlqUXlOamRsWXpNQHgudG15dW5zdWIueHl6OjM4MDIxIyVFNSU4RiVCMCVFNiVCOSVCRSUyMCU3QyUyMElFUEwlRTQlQjglOTMlRTclQkElQkYNCnNzOi8vWTJoaFkyaGhNakF0YVdWMFppMXdiMng1TVRNd05Ub3haVGxtWlRWak5pMWxNelF6TFRSbVkyUXRZbUl4TmkxaVkySTFZalF5TmpkbFl6TUB4LnRteXVuc3ViLnh5ejozODAzMSMlRTYlOTclQTUlRTYlOUMlQUMlMjAlN0MlMjBJRVBMJUU0JUI4JTkzJUU3JUJBJUJGDQpzczovL1kyaGhZMmhoTWpBdGFXVjBaaTF3YjJ4NU1UTXdOVG94WlRsbVpUVmpOaTFsTXpRekxUUm1ZMlF0WW1JeE5pMWlZMkkxWWpReU5qZGxZek1AeC50bXl1bnN1Yi54eXo6MzgwMzIjJUU2JTk3JUE1JUU2JTlDJUFDMiUyMCU3QyUyMElFUEwlRTQlQjglOTMlRTclQkElQkYNCnNzOi8vWTJoaFkyaGhNakF0YVdWMFppMXdiMng1TVRNd05Ub3haVGxtWlRWak5pMWxNelF6TFRSbVkyUXRZbUl4TmkxaVkySTFZalF5TmpkbFl6TUB4LnRteXVuc3ViLnh5ejozODA0MSMlRTYlOTYlQjAlRTUlOEElQTAlRTUlOUQlQTElMjAlN0MlMjBJRVBMJUU0JUI4JTkzJUU3JUJBJUJGDQpzczovL1kyaGhZMmhoTWpBdGFXVjBaaTF3YjJ4NU1UTXdOVG94WlRsbVpUVmpOaTFsTXpRekxUUm1ZMlF0WW1JeE5pMWlZMkkxWWpReU5qZGxZek1AeC50bXl1bnN1Yi54eXo6MzgwNTEjJUU5JTlGJUE5JUU1JTlCJUJEJTIwJTdDJTIwSUVQTCVFNCVCOCU5MyVFNyVCQSVCRg0Kc3M6Ly9ZMmhoWTJoaE1qQXRhV1YwWmkxd2IyeDVNVE13TlRveFpUbG1aVFZqTmkxbE16UXpMVFJtWTJRdFltSXhOaTFpWTJJMVlqUXlOamRsWXpNQHgyLnRteXVuc3ViLnh5ejozODA1MiMlRTklOUYlQTklRTUlOUIlQkQyJTIwJTdDJTIwSUVQTCVFNCVCOCU5MyVFNyVCQSVCRg0Kc3M6Ly9ZMmhoWTJoaE1qQXRhV1YwWmkxd2IyeDVNVE13TlRveFpUbG1aVFZqTmkxbE16UXpMVFJtWTJRdFltSXhOaTFpWTJJMVlqUXlOamRsWXpNQHgudG15dW5zdWIueHl6OjM4MDYxIyVFNyVCRSU4RSVFNSU5QiVCRCUyMCU3QyUyMElFUEwlRTQlQjglOTMlRTclQkElQkYNCnNzOi8vWTJoaFkyaGhNakF0YVdWMFppMXdiMng1TVRNd05Ub3haVGxtWlRWak5pMWxNelF6TFRSbVkyUXRZbUl4TmkxaVkySTFZalF5TmpkbFl6TUB4LnRteXVuc3ViLnh5ejozODA5MSMlRTglOEIlQjElRTUlOUIlQkQlMjAlN0MlMjBJRVBMJUU0JUI4JTkzJUU3JUJBJUJGDQo=")
repo.index.commit('update cyou content')

repo.remote().push()