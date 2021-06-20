'''
chapter4 操作列表
'''

#  4.1 遍历列表 for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#  4.1.1 深入的研究循环
#  4.1.2 在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("i can't wait to see your next tric" + magician.title() + '.\n')

# 4.1.3 在for循环结束后执行一些操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("i can't wait to see your next trick" + magician.title() + '.\n')
print('thanks everyone，that was a great show')  # 不缩进 将在循环结束后执行

# 4.2 避免缩进错误
'''
一些常见的缩进错误：
1.忘记缩进-python使用缩进代码行与前一个代码行的关系;
2.忘记缩进额外的代码行-注意你的逻辑，你要对便利出来的每个元素执行操作，还是要在循环结束后，执行操作；
3.不必要的缩进
4.遗忘了for之后的冒号
'''

# 4.3 创建数值列表
# 4.3.1 使用函数range()生成一系列数字
for number in range(1, 5):  # 左闭右开 ，实际上会打印1，2，3，4 而不会打印出5
    print(number)
for number2 in range(5):  # 会打印1，2，3，4
    print(number2)

# 4.3.2 使用range() 创建数字列表
numbers = list(range(6))  # list() 函数将range()转换为列表
print(range(6))
print(numbers)

# 使用range()可以指定步长
even_number = list(range(2, 11, 2))
print(even_number)

# 将1-10的整数的平方放到一个列表中
squars = []
for value in range(1, 10):
    squar = value ** 2
    squars.append(squar)
print(squars)

# 更简洁的写法
squars = []
for value in range(1, 10):
    squars.append(value ** 2)  # 不使用临时变量
print(squars)

# 4.3.3 对数字列表执行更简单的统计计算
digit = range(1, 11)
digit1 = list(range(1, 11))
print(digit)  # range(1, 11)
print(digit1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digit1))  # 1
print(max(digit1))  # 10
print(sum(digit1))  # 55
print(min(digit))  # 1
print(max(digit))  # 55
print(sum(digit))  # 55

# 4.3.4 列表解析
# 列表解析将for循环和创建新元素的代码合并为一行，并且自动附加新元素
squars2 = [value ** 3 for value in list(range(1, 11))]
print(squars2)

# 使用for打印1-20 .
number = [value * 1 for value in range(1, 21)]
print(number)

# 打印1-1000000
million = [value for value in range(1, 50)]
print(million)

# 打印1-20之间的奇数
odd_number = list(range(1, 21, 2))
print(odd_number)

# 3的倍数
Triples = []
for value in range(1, 31):
    if value % 3 == 0:
        Triples.append(value)
print([value for value in Triples])

# 4.4 使用列表的一部分 (列表的部分元素 - 切片)
# 4.4.1 切片
players = ['赵四', '刘能', '谢广坤', '王大脑袋', '菜虚鲲']
print(players[0:3])  # 切片包含索引为0，1，2的元素
print(players[:4])  # 如果没有指定开始索引，将从头开始
print(players[2:])  # 如果么有指定结束索引，将一直到末尾
print(players[:])  # [:] 切片将包含列表所有元素
print(players[-3:])  # 输出列表最后三个元素

# 4.4.2 遍历切片
players = ['赵四', '刘能', '谢广坤', '王大脑袋', '菜虚鲲']
print('有请前三位出场：')
for superStar in players[:3]:
    print(superStar)

# 4.4.3 TODO
