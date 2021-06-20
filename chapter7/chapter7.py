"""
chapter7 用户输入和while循环

"""
# 7.1 函数 input()的工作原理:函数input()让程序暂停运行，等待用户输入一些文本
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 7.1.1 编写清晰的程序
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# 7.1.2 使用 int()来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 7.1.3 求模运算符
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7.2 while 循环简介
# 7.2.1 使用 while 循环
number = 1
while number <= 5:
    print(number)
    number += 1

# 7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# 7.2.3 使用标志 -让while循环更简洁
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
flag = True
while flag:
    message = input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(message)

# 7.2.4 使用 break 退出循环
number = 1
while number < 7:
    print(number)
    number += 1
    if number == 3:
        break

print("--------------------")
number = 1
while number < 7:
    print(number)
    number += 1
    if number == 3:
        continue

# 7.2.5 在循环中使用 continue
# 打印10以内的所有奇数
print("--------------------")
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# 7.2.6 避免无限循环 小心处理while循环，防止无限循环

# 7.3 使用 while 循环来处理列表和字典
# 7.3.1 在列表之间移动元素
# 假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
print("--------------------")
unconfirmed_users = ['zhangsan', 'lisi', 'wangwu']
confirmed_users = []
while len(unconfirmed_users) != 0:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)
    print(user + "be confirmed")
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 7.3.2 删除包含特定值的所有列表元素
print("7.3.2 --------------------")
users = ['zhangsan', 'lisi', 'wangwu', 'zhangsan2']
print(users)
for user in users:
    if user.startswith("zhangsan"):
        users.remove(user)
print(users)

print("7.3.2 2--------------------")
users = ['zhangsan', 'lisi', 'wangwu', 'zhangsan2']
print(users)
for user in users:
    while user.startswith("zhangsan"):
        users.remove(user)
        break  # 小心while循环带来的问题，少使用while循环
print(users)

# 7.3.3 使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


