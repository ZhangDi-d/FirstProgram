# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)

before_one_day = timedelta(1)
yesterday = now - before_one_day
print(before_one_day)
print(yesterday)

print(now, type(now))

'''
时间对象转字符串 strftime
'''

now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str, type(now_str))

now_str_2 = now.strftime('%Y/%m/%d %H/%M/%S')
print(now_str_2, type(now_str_2))

'''
字符串转时间类型 strptime
'''
print('--------------')
now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
date_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print(date_obj, type(date_obj))
