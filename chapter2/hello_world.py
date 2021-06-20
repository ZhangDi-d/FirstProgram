"""
chapter2 变量和简单数据类型
"""
# 2.1 hello world
print("hello world")

# 2.2 变量
message = "hello python world!"
print(message)

message = "hello python crash Course world!"
print(message)

# 2.2.1 python中变量应该尽量使用小写 避免不合理的命名

# 2.3 字符串
message1 = 'i am good "man"'
message2 = "i am 'good' man "
message3 = "i am good man"
message4 = 'i am good man '

# 2.3.1 字符串的大小写
name1 = 'ada lovelace'
print(name1.title())  # .title() 以首字母大写的方式显示每个单词
name2 = "Ada Lovelace"
print(name2.upper())
name3 = "Ada Lovelace"
print(name3.lower())

# 2.3.2 合并字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + last_name
full_name2 = first_name + " " + last_name
print(full_name)
print(full_name2)
print('hello,' + full_name2.title() + "!")

# 2.3.3 使用制表符或者换行符来添加空白
print('python')
print('\tpython')  # \t 制表符

print('python')
print('languages:\npython\nc\njava')  # \换行符

# 2.3.4 删除空白
favorite_language = 'python '
print(favorite_language + "!")  # python !
print(favorite_language.rstrip() + "!")  # python!  使用rstrip去除字符串末尾的空白

favorite_language1 = ' python '
print("!" + favorite_language1)  # ! python
print("!" + favorite_language1.lstrip())  # !python 使用lstrip去除字符串末尾的空白

favorite_language2 = ' python '
print("!" + favorite_language2 + '!')
print("!" + favorite_language2.strip() + '!')  # !python! 使用strip去除字符串前后的空格

# 2.4 数字
# 2.4.1 整数
print(100 + 200)
print(100 - 200)
print(0.1 - 0.2)
print(200 * 100)
print(0.1 * 2)
print(3 / 2)
print(2 ** 4)  # 2的4次方

#  2.4.2 浮点数
print(0.1 * 0.2)  # 0.020000000000000004
print(0.3 / 0.2)  # 1.4999999999999998
print(0.1 + 0.2)  # 0.30000000000000004
print(3 * 0.1)  # 0.30000000000000004

#  2.4.3 使用str()函数避免类型错误
age = 23
# message = 'happy ' + age + "birthday!"
# print(message)  # TypeError: can only concatenate str (not "int") to str
message = 'happy ' + str(age) + "birthday!"
print(message)

# 2.5 注释
# 你好
print('你好')

'''
你好吗
'''
print('你好吗')

import this # module level import should be located at the top of this file
print(this)
'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


