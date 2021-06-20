# coding: utf-8

class Parent(object):
    def __init__(self, object):
        print('hello i am parent %s' % object)


class Child(Parent):  # 需要加Parent 否则无法继承
    def __init__(self, c, p):
        print('hello i am child %s' % c)
        super(Child, self).__init__(p)


class Child1(Parent):
    def __init__(self, c1):
        print('hello i am child %s' % c1)
        super(Child1, self).__init__('p1')


if __name__ == '__main__':
    c = Child('c', 'p')

    c1 = Child1('c1')
