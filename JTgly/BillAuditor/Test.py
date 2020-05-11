# -*- coding: utf-8 -*-
import requests
import json

class web_requests(object):
    def __init__(self):
        pass

    def Interface(self,Interface_path,**My_data):
         url = "https://devapi.lanycee.com/api/v1/login/login/%s"%(Interface_path) # 测试的接口url
         headers = {"Host": "devapi.lanycee.com",
                    "Accept": "application/json, text/plain, */*",
                    "Referer": "https://dev.lanycee.com/login/",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Origin": "https://dev.lanycee.com",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "application/json, text/plain, */*",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
         #data1 = {"beginDate": "2018-01-01", "endDate": "2018-04-01"}  # 接口传送的参数
         data = My_data  # 接口传送的参数
         r = requests.get(url=url, json=data, headers=headers)  # 发送请求
         # return r.json
         print(r.text)  # 获取响应报文
         print(r.status_code)

a = web_requests()
a.Interface('%s', mobile="19817146896", platform="admin", loginCode="0000")