# -*- coding: utf-8 -*-
"""
chapter5 if语句
"""
# 5.1 一个简单示例
cars = ['audi', '漏油benz', 'bmw', 'toyota']
for car in cars:
    if car == 'bmw':  # 判断字符串字面量相等
        print(car.upper())
    else:
        print(car.title())

# 5.2 条件测试  :每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。
# 5.2.1 检查是否相等
car = 'bmw'
print(car == 'bmw')  # true

# 5.2.2 检查是否相等时不考虑大小写
# 在Python中检查是否相等时区分大小写
car = 'Audi'
print(car == 'audi')  # False

# 5.2.3 检查是否不相等  :要判断两个值是否不等，可结合使用惊叹号和等号（!=）
name = '李四'
if name == '张三':
    print('你是张三')
else:
    print('你不是张三')

# 5.2.4 比较数字
answer = 17
if answer != 42:
    print('你的答案是错误的,宇宙的终极秘密是42,不是%s!' % answer)
else:
    print('你看破了宇宙!!!')

# 5.2.5 检查多个条件
# 1. 使用and检查多个条件
age = 10
if age < 30 and age < 40:
    print("aa")
else:
    print("bb")

if (age < 50) & (age < 60):
    print("cc")
else:
    print("dd")

# 2. 使用or检查多个条件
age_1 = 20
if (age_1 > 10) | (age_1 > 15):
    print("ee")
else:
    print("ff")

# 5.2.6 检查特定值是否包含在列表中   in
grade = ['甲', '乙', '丙']
mina = '丁'
if min in grade:
    print('good-level')
else:
    print('bad-level')

# 5.2.7 检查特定值是否不包含在列表中   not in
grade = ['甲', '乙', '丙']
zhao_level = '丁'
if zhao_level not in grade:
    print('bad-level')
else:
    print('good-level')

# 5.2.8 布尔表达式
# True/False

# 5.3 if 语句
# 5.3.1 简单的 if 语句
age = 19
if age >= 18:
    print("You are old enough to vote!")

# 5.3.2 if-else 语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 5.3.3 if-elif-else 结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 5.3.4 使用多个 elif 代码块
age = 12
price
if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 20
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 5.3.5 省略 else 代码块
# Python并不要求if-elif结构后面必须有else代码块:else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，
# 这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。

# 5.3.6 测试多个条件
request_word = ['花', '好', '月', '圆']
need_words = ['花', '好', '月', '圆']
finish_words = []
for need_word in need_words:
    if need_word in request_word:
        print("need %s" % need_word)
        finish_words.append(need_word)
print("GOOD" if len(finish_words) > 2 else "BAD")  # python中没有三元运算符，可以用这种格式替代

# 5.4 使用 if 语句处理列表
# 5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5.4.2 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3 使用多个列表
available_words = ['小', '英', '雄', '雨', '来']
request_words = ['小', '英', '雄', '哪', '吒']
for request_word in request_words:
    if request_word in available_words:
        print('我们有这个word：%s' % request_word)
    else:
        print('我们么有这个word:%s' % request_word)

# 5.5 设置 if 语句的格式
# PEP 8提供的唯一建议是，在诸如==、 >=和<=等比较运算符两边各添加一个空格，例如， if age < 4:要比if age<4:好
