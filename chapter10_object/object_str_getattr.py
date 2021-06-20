# coding: utf-8

class Person(object):
    def __str__(self):
        print('__str__ 类的描述信息')
        return 'person'

    # key 任意不存在的属性名
    def __getattr__(self, key):
        print('key {} not exist'.format(key))


if __name__ == '__main__':
    p = Person()
    p.a
    print(p)  # __str__,类似于 java里的toString
