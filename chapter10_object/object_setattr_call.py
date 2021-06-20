# coding: utf-8

'''
__setattr__ 拦截不存在属性，并为其设置值
'''


class Person(object):
    def __getattr__(self, item):
        print('__getattr__ {}'.format(item))
        return 'iterm {}'.format(item)

    def __setattr__(self, key, value):
        # if key not in self.__dict__:
        self.__dict__[key] = value
        print(self.__dict__)

    def __str__(self):
        print('__str__ 类的描述信息')

    def __call__(self, *args, **kwargs):
        print('call will start')
        print('args is {}'.format(args))
        print('args is {}'.format(kwargs))
        pass


# if __name__ == '__main__':
p = Person()
p.a
p.name = 'lisi'  # __setattr__
print(p.name)

p('zhangsan')


# 链模式操作
class Person2(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __call__(self, name):
        # print('key is {}'.format(self.__attr))
        return name

    def __getattr__(self, item):
        if self.__attr:
            item = '{}.{}'.format(self.__attr, item)
        else:
            item = item
        print(item)
        return Person2(item)


t2 = Person2()
t2.a

t2.a.b.c


name = t2.a.b.c('lisi')
print(name)
