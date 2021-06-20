# coding:utf-8

def test1(number):
    if number == 100:
        raise ValueError('number 不可以 是 100')
    else:
        return number


result = test1(20)


def test2(number):
    try:
        return test1(number)
    except ValueError as e:
        return e
    finally:
        print("finally")


result2 = test2(100)
print(result2)


def test3(number):
    raise 'error test3'


# test3(100)


# 自定义一个异常类

class NameLimitError(BaseException):
    def __init__(self, message):
        self.message = message


class NumberLimitError(BaseException):
    def __init__(self, message):
        self.message = message


def test5(name):
    if name == 'lisi':
        raise NameLimitError('lisi 不能是name')
    return name


print('===========')

try:
    test5('lisi')
except NameLimitError as ne:
    print(type(ne))
