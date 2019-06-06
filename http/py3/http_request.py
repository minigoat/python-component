#! python3
# coding: utf-8

"""
http基础方法

Rules:
1. POST/DELETE/PUT: json in - json out, 如果resp.json报错，则是接口问题
2. GET带参数 HEAD不带参数
3. 以统一的header头发送请求
"""

from urllib import request

class httpRequest:
    def _http_request(self, method, url, headers=None, data=None):
        try:
            req = request.Request(url)
            req.add_header('Content-Type', 'application/json')
            if method == "GET":
                with request.urlopen(req) as response:
                    data = response.read()
            else:                
                return False, None
        except Exception as e:
            print("request error! method: %s, url: %s, data: %s, response_status: %s, response_content: %s" % (method, url, str(data), response.status, data.decode('utf-8')))            
            return False, None
        else:
            if response.status != 200:
                print("request status not equal to 200! method: %s, url: %s, data: %s, response_status: %s, response_content: %s" % (method, url, str(data), response.status, data.decode('utf-8')))
                return False, None
            return True, data.decode('utf-8')

    def http_get(self, url): 
        return self._http_request(method="GET", url=url)
