# coding:utf-8

class Person(object):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person(name='libai', age=12)
person1.name = "lisi"
print('name = %s ,age = %d' % (person1.name, person1.age))
