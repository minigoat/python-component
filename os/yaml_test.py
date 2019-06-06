#! python2
# coding: utf-8

import yaml

if __name__ == '__main__':
   f = open('./conf/conf.yaml')
   res = yaml.load(f)
   print(res)
   f.close