# coding:utf-8

'''
类的私有函数和私有变量：
1. 无法被实例化之后的对象调用的函数和变量
2. 类内部可以调用函数和变量
3. 只是希望被类内部使用，不希望被使用者调用

'''


class Test(object):
    pass  # 占位符


class Person(object):
    name = None
    username  = None
    __password = None
    def __init__(self, name):
        self.name = name
        self.username = name
        self.__password = 123456

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return f'person {self.name} {self.__password} jumping'

    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return f'person {self.name} {self.__password}running'


person = Person(name="lisi")
person.name = 'libai'

person.jump()
person.run()
# person.__run() #  'Person' object has no attribute '__run'


print(dir(person))
print(person._Person__run)  # 实例化对象可以调用类的私有函数 ，但是不推荐

print(person._Person__password)