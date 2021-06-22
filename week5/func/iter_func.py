# coding:utf-8
"""
iter(iterable)

yield
"""


def _next(iter_obj):
    try:
        return next(iter_obj)
    except:
        return None


iter_0 = iter([1, 2, 3])
result = next(iter_0)
print(result)

print(_next(iter_0))
print(_next(iter_0))
print(_next(iter_0))
print(_next(iter_0))

res = (i for i in (1, 2, 3))  # 通过for循环创建了一个迭代器
print(next(res))

print('============')


def make_iter(iter_obj):  # 通过yield创建了一个迭代器
    for data in iter_obj:
        yield data


iter_3 = make_iter([1, 2, 3])
print(next(iter_3))
