# coding:utf-8

"""

三个魔法函数
filter(func,list) 使用 func对lsit进行判断
map(func,list)  boolean转换
reduce(func,list)
"""

from functools import reduce

res_0 = filter(lambda x: x > 1, [0, 1, 2, 2])
print(list(res_0))

res_1 = map(lambda x: x > 1, [0, 1, 2, 2])
print(list(res_1))

res_2 = reduce(lambda x, y: x + y, [0, 1, 2, 2])
print(res_2)

fr = ['aba', 'abb', 'acd']
res_4 = filter(lambda x: 'b' in x, fr)
print(list(res_4))
