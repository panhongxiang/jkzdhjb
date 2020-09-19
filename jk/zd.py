import requests    #导入requests  包

# res = requests.get(url="http://192.168.2.124:8081/area/listarea")   #接口发起查看全部请求
# res2 = requests.get(url="http://192.168.2.124:8081/area/getareabyid",params = {"areaId":"1"}) #查单个
# print(res.status_code)   #打印状态码
# print(res.json(),res2.json())    # 打印接口响应数据


# tj ={"areaName" : "南部","priority" : "1"}
# res3 = requests.post(url="http://192.168.2.124:8081/area/addarea/",data=tj)   #接口发起添加数据请求
# print("状态码",res3.status_code)
# print("响应体",res3.text)

# xg = {
#     "areaId": 2,
#     "areaName": "南部西",
#     "priority": "2"}
# res5 = requests.put(url= "http://192.168.2.124:8081/area/modifyarea",json=xg)   #接口修改数据请求
#
# print("状态码",res5.status_code)
# print("响应体",res5.text)

# res6 = requests.delete(url="http://192.168.2.124:8081/area/removearea/", params={"areaId": 2})
# print("状态码",res6.status_code)
# print("响应体",res6.json())

# res1 = requests.get(url="http://www.baidu.com")
# print(res1.text)

