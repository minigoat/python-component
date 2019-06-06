#! python2
# coding: utf-8

import logging
# from urllib import request
from http_request import HTTPClient

def main():
    print('--- start')
    logging.basicConfig(filename="log/app.log", level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Start")
    http = HTTPClient()
    result = http.get('http://rap2api.taobao.org/app/mock/9836/query/redis_ip_list')
    print("result", result)
    logger.info("result: %s" % result)
    logger.info("Finish")
    print('--- end')
    
if __name__ == '__main__':
	main()