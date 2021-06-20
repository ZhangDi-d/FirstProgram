"""
chapter 9 类
Python中，首字母大写的名称指的是类。
类中的函数成为方法，类中的函数称为方法；你前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式
"""

# 9.1 创建和使用类
# 9.1.1 创建dog类
'''
为何必须在方法定义中包含形参self呢？因为
Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
'''


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting now!")

    def roll_over(self):
        print(self.name.title() + " is rolling over ~")


# 9.1.2 根据类创建实例
'''
方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例。我们将这
个实例存储在变量my_dog中
'''
myDog = Dog("bo", 4)
print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old.")
myDog.sit();
