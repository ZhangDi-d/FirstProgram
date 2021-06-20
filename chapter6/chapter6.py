"""
chapter6 字典
- 1.在Python中， 字典是一系列键—值对。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
- 2.注意，键—值对的排列顺序与添加顺序不同。 Python不关心键—值对的添加顺序，而只关心键和值之间的关联关系。
- 3.空字典  {}
- 4.1增加 dict[new_key] = new_value
- 4.2修改字典的value，只需对key重新赋值即可 dict[key] = new_value
- 4.3删除 删除键— 值对 del dict[key_need_removed]
- 4.4查询 dict[key_wanted]
- 5. 遍历
- 5.1for key_var, value_var in dict.items():
- 5.2遍历所有键：for key_var in dict.keys():
- 5.3遍历所有值：for value_var in dict.values():
- 5.4按顺序遍历所有的键：可使用函数sorted()来获得按特定顺序排列的键列表的副本： for key_var in sorted(dict.keys()):
- 5.5对值去重：set() ：for value_var in set(dict.values()):
- 6 嵌套: 将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套

"""

# 6.1 一个简单的字典
alien_0 = {"color": "blue", "age": 500}
print(alien_0["color"])
print(alien_0['color'])  # 单双引号都可以

# 6.2 使用字典 :
# 在Python中， 字典是一系列键—值对。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。

# 6.2.1 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 6.2.2 添加键—值对
alien_1 = {'color': 'green', 'points': 5}
alien_1['x_position'] = 0
alien_1['y_position'] = 23
print(alien_1)

# 6.2.3 先创建一个空字典
alien_2 = {}
alien_2['color'] = 'green'
alien_2['point'] = 10
print(alien_2)

# 6.2.4 修改字典中的值
alien_1 = {'color': 'green', 'points': 5}
alien_1['color'] = 'red'
print(alien_1)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 6.2.5 删除键— 值对
alien_1 = {'color': 'green', 'points': 5}
del alien_1['color']
print(alien_1)
# delattr(alien_1, 'points') # AttributeError: 'dict' chapter10_object has no attribute 'points'
# print(alien_1)

# 6.2.6 由类似对象组成的字典
favorite_languages = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby'
}
print(favorite_languages)

# 6.3 遍历字典
# 6.3.1 遍历所有的键— 值对
user_0 = {
    'username': '张三',
    '姓': '张',
    '名': '三',
}
for key, value in user_0.items():  # key,value是对应的键值的变量，可以随意设置
    # print("user_0[key]" + user_0[key] + ",user_0[value]" + user_0[value])  #  too many values to unpack (expected 2)
    print("user_0[key]:" + key + ",user_0[value]:" + value)
for a, b in user_0.items():
    print("user_0[key]:" + a + ",user_0[value]:" + b)

favorite_languages = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby'
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# 6.3.2 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
# 遍历字典中的所有值
for name1 in favorite_languages.values():
    print(name1.title())
print('------------------------------')
favorite_languages_2 = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby'
}
friends = ['lisi', 'zhangsan']
for name in favorite_languages_2.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages_2[name].title() + "!")
print('------------------------------')
# 6.3.3 按顺序遍历字典中的所有键
favorite_languages_2 = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby'
}
for name in sorted(favorite_languages_2):
    print(name.title())
    print(name.title() + ", thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值
# values()，它返回一个值列表，而不包含任何键
print('------------------------------')
favorite_languages_3 = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby'
}
for language in sorted(favorite_languages_3.values()):
    print(language.title())
# 这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，
# 但如果被调查者很多，最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）
print('------------------------------')
favorite_languages_4 = {
    'zhangsan': 'java',
    'lisi': 'go',
    'wangwu': 'ruby',
    'simayi': 'java'
}
for language in set(favorite_languages_4.values()):
    print(language.title())

# 6.4 嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套
# 6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print('------------------------------')
# 我们使用range()生成了30个外星人
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_num in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
    print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

print('------------------------------')
# 要将前三个外星人修改为黄色的、速度为中等且值10个点，
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
    print("...")

# 6.4.2 在字典中存储列表
classroom = {
    '年纪': '初一',
    '班主任': "zhangsan",
    'student': ['张晓明', '李雷']
}
for student in classroom['student']:
    print(student.title())
print('------------------------------')
favorite_languages = {
    'zhangsan': ['python', 'ruby'],
    'lisi': ['c'],
    'wangwu': ['ruby', 'go'],
    'qinliu': ['python', 'go'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# 6.4.3 在字典中存储字典
classroom = {
    'basic_information': {'grade': '初一', '班主任': 'zhangsan'},
    'student_information': {'No.1': '韩梅梅', 'NO.2': ['赵峰', 'lisi']}
}
for info,info1 in classroom.items():
    print(info)
    print(info1)


room = [['lisi'],'wangwu']
print(room)