# coding:utf-8

def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()

    except:
        print('exception str_data {} 不是str类型'.format(str_data))
    return new_str


result = upper(1)
print('result:', result)


def upper2(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()

    except Exception as e:
        print('{}'.format(e))
        print('exception str_data {} 不是str类型'.format(str_data))
    return new_str


result = upper2(1)
print('result2:', result)


def test():
    try:
        print(name)
        1 / 0
        print('go on')
    except ZeroDivisionError as e:
        print(e.__str__())
    except NameError as e1:
        print(e1.__str__())


test()


def test1():
    try:
        print(name)
        1 / 0
        print('go on')
    # 多种异常
    except (ZeroDivisionError, NameError)as e:
        print(e)
        print(type(e))


test1()
