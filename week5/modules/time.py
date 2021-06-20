# coding:utf-8
import time
from datetime import datetime

time_ = time.time()
print(time_)
print(time_, type(time_))

local_ = time.localtime(time_)
print(local_)
print(local_, type(local_))

before_1000 = time_ - 1000
before_1000_obj = time.localtime(before_1000)
print(before_1000_obj, type(before_1000_obj))

time.sleep(1)

print('after 10 secs')

'''
time ->string
'''

now = time.localtime()
now_str = time.strftime('%Y-%m-%d %H:%M:%S', now)
print(now_str, type(now_str))

'''
string ->time
'''
now_obj = time.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print(now_obj, type(now_obj))

print('==================')
'''
datetime 时间戳
'''
now = datetime.now()
ts = datetime.timestamp(now)
print(ts, type(ts))

now_from_ts = datetime.fromtimestamp(ts)
print(now_from_ts, type(now_from_ts))
