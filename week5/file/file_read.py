# coding:utf-8
"""
r 读取文件
rb 二进制形式读取文件

f.read()

f.readlines()

f.readline() 每次返回一行

f.mode  文件模式
f.name  文件名称
f.closed 文件是否关闭


"""
import os


def read(self, is_strip=True):
    with open(self.path, mode=self.mode) as f:
        data = f.read()
    print(data)


target_path = os.getcwd() + "/a.txt"
f = open(target_path, "r")
line = f.read()

print(line)
f.close()
print('-----------')
target_path = os.getcwd() + "/a.txt"
f = open(target_path, "r")
line = f.readline()
print(line)
