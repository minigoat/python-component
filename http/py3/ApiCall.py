#! python3
# coding: utf-8

import logging
# from urllib import request
from http_request import httpRequest

def main():
    print('--- start')
    logging.basicConfig(filename="log/app.log", level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Start")
    http = httpRequest()
    result, data = http.http_get('http://rap2api.taobao.org/app/mock/9836/query/redis_ip_list')
    print("result", result)
    print("data", data)
    logger.info("result: %s" % result)
    logger.info("data: %s" % data)
    logger.info("Finish")
    print('--- end')
    
if __name__ == '__main__':
	main()