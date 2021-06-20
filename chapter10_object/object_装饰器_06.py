# coding:utf-8

'''
装饰器

外围函数和内嵌函数

定义规则
def outer(func_args):              # 外围函数
    def inner(*args,**kwargs):     # 内嵌函数
        return func_args(*args,**kwargs)
    return inner  外围函数中返回内嵌函数
'''


def check_str(func):
    def inner(*args, **kwargs):  # 内嵌函数
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s ' % result
        else:
            return 'result is failed : %s' % result

    return inner


@check_str
def test(data):
    return data


result = test('no')
print(result)

resutl1 = test('ok')
print(resutl1)
