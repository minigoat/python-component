#! python2
# coding: utf-8

"""
http基础方法
"""
import urllib
import urllib2
import json

class HTTPClient:
    def __init__(self):
        self.headers = {'Content-type': 'application/json'}
    
    def set_headers(self, headers):
        self.headers = headers

    def get(self, url, params=None):
        try:
            if params != None:
                params = urllib.urlencode(params)
                url = url + "?" + params
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read()            
            if response.getcode() == 200:
                print('content', content)
                result = json.loads(content)
                return result
            else:
                return {'result': False, 'code': response.getcode(), 'message': content}
        except Exception as e:
            print('e', e)
            return {'result': False, 'code': 500, 'message': str(e)}

    def post(self, url, params={}):
        try:
            params = urllib.urlencode(params)
            request = urllib2.Request(url, data=params, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read()
            if response.getcode() == 200:
                result = json.loads(content)
                return result
            else:
                return {'result': False, 'code': response.getcode(), 'message': content}
        except Exception as e:
            return {'result': False, 'code': 500, 'message': str(e)}
