# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify GET
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login POST
# 登录提交的参数: {"username":"xxxxx","password":"yyyy","verify_code":"zzzz"},非 JSON 提交
# 我的订单：http://localhost/Home/Order/order_list.html GET
import requests

res = requests.Session()
response = res.get(url= "http://192.168.2.20/index.php?m=Home&c=User&a=verify")
print(response.status_code)
# print(response.text)

data = {"username": "13599999999", "password": "123456", "verify_code": "8888"}
res1= res.post(url= "http://192.168.2.20/index.php?m=Home&c=User&a=do_login",data=data)
print(res1.status_code)
print(res1.text.encode('utf-8').decode('unicode_escape'))

res2 = res.get(url= "http://192.168.2.20/Home/Order/order_list.html")
print(res2.status_code)
print(res2.text)