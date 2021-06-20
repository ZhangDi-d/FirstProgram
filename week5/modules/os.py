# coding:utf-8

import os

print(os.getcwd())

print(os.listdir('C://Users//zhangdi//Desktop//Steam'))

new_path = '%s/test1' % os.getcwd()
# os.makedirs(new_path)
print(new_path)

curdir = os.path.curdir
print(curdir)
