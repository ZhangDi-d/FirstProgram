# coding:utf-8

'''
继承
'''


class Person(object):
    name = None

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Person.name = name + '1'  # 类变量与实例变量的区别

    def talk(self):
        print('talk')

    def eat(self):
        print('eat')


class Child(Person):
    def swim(self):
        print('swim')


p = Person(name="libai", sex='male')
p.eat()
print(p.name)
print(Person.name)

child = Child(name="lisi", sex='male')
child.swim()
