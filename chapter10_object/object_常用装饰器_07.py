# coding:utf-8

'''
classmethod 不通过实例化调用类函数

@classmethod
def func(cls,...):
    do

'''


class Test(object):
    def __init__(self, a):
        self.a = a

    def run(self):
        print('run')
        self.jump()  # 不会报错

    @classmethod  # 带有@classmethod 的函数 不能调用带有self的普通的类函数 ，反之却可以
    def jump(cls):
        print('jump')
        # cls.run()  # 会报错 3. run() missing 1 required positional argument: 'self'


t = Test('a')
t.run()

# Test.run()  # 1. missing 1 required positional argument: 'self'
# 会报错，没有类的实例化 不能调用类函数


Test.jump()  # 2. 使用classmethod可以不实例化调用类函数

'''
staticmethod

函数可以不经过实例化而被直接调用 ，
被该装饰器调用的函数不能传递self或者clas参数
并且无法在该函数内调用其他类函数或者类变量 （可以理解为 java中的static）

普通的函数可以调用 @classmethod 或者 @staticmethod 装饰器函数 

@staticmethod
def func(...):
    do 
'''


class Person(object):
    @staticmethod
    def sleep():  # 没有self .所以无法调用 函数

        print('sleep')


p = Person()
p.sleep()  # 实例调用
Person.sleep()  # 类调用

'''

@property 把被修改的方法装饰为一个属性 

@property
def func(self):
    do 
'''


class Student(object):
    def __init__(self, name):
        self.name = name

    @property
    def call_name(self):
        print('hello {}'.format(self.name))
        return f'hello {self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter  # 对返回值self.__name进行调整
    def name(self, value=None):
        self.__name = value

s = Student(name="libai")
result = s.call_name
print(result)
