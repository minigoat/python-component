#! python2
# coding: utf-8

import json

if __name__ == '__main__':
   with open('./conf/conf.json', mode='r') as f:
        print('f', f)
        print('type(f)', type(f))
        k = f.read()
        # print('k', k)
        # print('type(k)', type(k))
        res = json.loads(k)
        print('res', res)
        print('type(res)', type(res))
        f.close