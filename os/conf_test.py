#! python2
# coding: utf-8

import ConfigParser

if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    cf.read('./conf/conf.ini')
    print('cf', cf)
    sections = cf.sections() # 获取配置文件所有的section
    print(u'section', sections)
    options = cf.options('mysql') # 获取指定section下所有option
    print(u'option', options)
    items = cf.items('mysql') # 获取指定section下所有的键值对
    print(u'items', items)
    value = cf.get('mysql', 'host') # 获取指定的section下的option
    print(u'value', value)