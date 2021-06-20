"""
chapter 8 函数
形参名*toppings中的星号让Python创建一个名为toppings的空元组
形参**user_info中的两个星号让Python创建一个名为user_info的空字典
"""


# 8.1 定义函数
def func_greet():
    print("hello")


func_greet()


# 8.1.1 向函数传递信息
def func_greet2(username):
    print("hello %s" % username)


func_greet2("张三")


# 8.1.2 实参和形参 概念类似java的实参和形参

# 8.2 传递实参
# 8.2.1 位置实参
def introduction(name, time):
    print(name)
    print(time)
    print("我叫%s,是练习%.1f的练习生,喜欢唱跳rap篮球." % (name, time))  # 保留2个小数位 %.2f


introduction("菜虚鲲", float("2.5"))


# 8.2.2 关键字实参
def introduction(name, time):
    print("我叫%s,是练习%.1f的练习生,喜欢唱跳rap篮球." % (name, time))  # 保留2个小数位 %.2f


introduction(name="菜虚鲲", time=float("2.5"))
introduction(time=float("2.5"), name="菜虚鲲")  # 关键字实参,传参时可以调整参数的先后位置


# 8.2.3 默认值 -编写函数时，可给每个形参指定默认值
# def introduction2(name='菜虚鲲', time):
#     print("我叫%s,是练习%.1f的练习生,喜欢唱跳rap篮球." % (name, time))  # 保留2个小数位 %.2f
#
#
# introduction2(time=float("2.5"))
# ## introduction2报错 :non-default argument follows default argument:这种错误原因是将没有默认值的参数在定义时放在了有默认值的参数的后面
# 由于给name指定了默认值，无需通过实参来指定name，因此在函数调用中只包含一个实参——time.然而，Python
# 依然将这个实参视为位置实参，因此如果函数调用中只包含time，这个实参将关联到函数定义中的第一个形参。这就是需要将time放在形参列表开头的原因所在
def introduction(time, name='菜虚鲲', ):
    print("我叫%s,是练习%.1f的练习生,喜欢唱跳rap篮球." % (name, time))  # 保留2个小数位 %.2f


introduction(time=float("3.5"))


# 8.2.4 等效的函数调用
def introduction(time, name='菜虚鲲', ):
    print('等效的函数调用')


introduction('1.5')
introduction(3)
introduction(time=float('1.2'), name='zhangsan')
introduction(1.2, 'lisi')


# 8.3 返回值
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行

# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


name = get_formatted_name("三", '张')
print(name)


# 8.3.2 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    return first_name + ' ' + middle_name + ' ' + last_name


# return full_name.title()
print(get_formatted_name('john', 'lee', 'hooker').title())


# 8.3.3 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    return {'名': first_name, '姓': last_name}


print(build_person('三', '张'))


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'名': first_name, '姓': last_name}
    if age:
        person[age] = age
    return person


musician = build_person('三', '张', age=27)
print(musician)


# 8.3.4 结合使用函数和 while 循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# while True:
#     print("\nTell me ur name")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if f_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")


# 8.4 传递列表
def greet_users(names):
    print(names)


names = ['zhangsan', 'lsii', 'wangwu']
greet_users(names)


# 8.4.1 在函数中修改列表
# 第一个函数将负责处理打印设计的工作，而第二个将概述打印了哪些设计：
def do_homework(undoWork, doneWork):
    while undoWork:
        current_work = undoWork.pop()
        doneWork.append(current_work)


def show_work(doneWork):
    for done in doneWork:
        print("我叫cxk，给你演示%s" % done)


undoWork = ['sing', 'dance', 'rap', 'basketball']
doneWork = []
do_homework(undoWork, doneWork)
show_work(doneWork)

# 8.4.2 禁止函数修改列表 (有时候，需要禁止函数修改列表,这时候可以使用切片)
print("----------------------------")


def do_homework(undoWork, doneWork):
    while undoWork:
        current_work = undoWork.pop()
        doneWork.append(current_work)


def show_work(doneWork):
    for done in doneWork:
        print("我叫cxk，给你演示%s" % done)


undoWork = ['sing', 'dance', 'rap', 'basketball']
doneWork = []
do_homework(undoWork[:], doneWork)
show_work(doneWork)
print("undoWork size:%d" % len(undoWork))
print("doneWork size:%d" % len(doneWork))

# 8.5 传递任意数量的实参  (类似于java中的可变参数)
print("----------------------------")


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

## 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。
print("----------------------------")


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print("for:" + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
print("----------------------------")


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.5.2 使用任意数量的关键字实参
print("----------------------------")


# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


user_profile = build_profile("三", '张', field1='math', field2='chinese')
print(user_profile)

# 8.6 将函数存储在模块中
# import语句允许在当前运行的程序文件中使用模块中的代码
# 8.6.1 导入整个模块
import pizza

print("8.6.1----------------------------")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.2 导入特定的函数
from pizza import make_pizza_fun

print("8.6.2----------------------------")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.3 使用 as 给函数指定别名
from pizza import make_pizza_fun as  mpf

print("8.6.2----------------------------")
mpf(16, 'pepperoni')
mpf(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.5 导入模块中的所有函数
from pizza import *
'''
使用并非自己编写的
大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相
同，可能导致意想不到的结果： Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而
'''

# 8.7 函数编写指南
'''
1.良好的命名
2.适当的注释
3.所有的import都应放在文件开头
4.实参与形参**
'''




















