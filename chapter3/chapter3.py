'''
chapter3 列表简介
'''

# 3.1 列表是什么 -列表中可以包含不同类型的元素。python使用[]表示列表。
program_languages = ['java', 'python', 'c++', 'Go']
print(program_languages)

# 3.1.1 访问列表元素
print(program_languages[0])  # java
print(program_languages[0].title())  # Java

print(program_languages[1])  # python
print(program_languages[3])  # Go

# 3.1.2 pyhton为访问末尾的元素提供了特殊的语法：索引为-1
# -1返回最后一个元素，同理-2返回倒数第二个元素，以此类推。
print(program_languages[-1])  # Go

#  3.1.3 使用列表中的各个值
message = 'my favorite  program language is ' + program_languages[-1]
print(message)

#  3.2 修改，添加和删除元素

# 3.2.1 修改列表元素
print(program_languages)
program_languages[0] = 'C'
print(program_languages)

# 3.2.2 在列表中添加元素
program_languages.append('Ruby')  # 在列表的末尾添加元素
print(program_languages)
program_languages.insert(0, 'VB')
print(program_languages)

# 3.2.3 在列表中删除元素
del program_languages[2]
print(program_languages)

# 2.使用pop删除元素
poped_pl = program_languages.pop()
print(poped_pl)

#  3.弹出列表中任何位置的元素
print(program_languages)
first_language = program_languages.pop(0)
print(first_language)

# 4.根据值删除元素
print(program_languages)
program_languages.remove('C')
print(program_languages)

program_languages.append('Go')
print(program_languages)
program_languages.remove('Go')
print(program_languages)  # remove方法只会删除第一个指定的'Go'元素

program_languages.append('C')
print(program_languages)

too_hard = 'C'
program_languages.remove(too_hard)
print(program_languages)

#  3.3 组织列表（顺序）
#  3.3.1 使用方法sort()对列表进行永久性排序
cars = ['牛逼BMW', '漏油benz', 'Auto', '奇瑞qq']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)  # 这种排序是永久性的

#  3.3.2 使用函数sorted()对列表进行临时性排序
cars = ['牛逼BMW', '漏油benz', 'Auto', '奇瑞qq']
print(cars)
#  临时性排序后
print(sorted(cars))
print(cars)

#  3.3.3 倒着打印列表
cars = ['牛逼BMW', '漏油benz', 'Auto', '奇瑞qq']
cars.reverse()
print(cars)  # reverse() 永久性的修改元素的排序

#  3.3.4 确定列表的长度
a = len(cars)
print(a)

#  3.4 使用列表时避免索引错误
print(cars[4])  # IndexError: list index out of range
