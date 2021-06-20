# 7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
# prompt = "\nWhat kind of car do you want to rent? "
# car = input(prompt)
# print("Let me see if I can find you a " + car + "!")

# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌。
# prompt = "\nHow many people do you have to eat? "
# guest_number = input(prompt)
# if int(guest_number) > 8:
#     print("There is no empty table here.")
# else:
#     print("Follow me ,pls")

# 7-3 10 的整数倍：让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
# prompt = "\ninput a number ,I can tell you if it is an integer multiple of 10 "
# number = int(input(prompt))
# if number % 10 == 0:
#     print("it is an integer multiple of 10。 ")
# else:
#     print("it  is not an integer multiple of 10。 ")
#

# 7-4 比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，
# 都打印一条消息，说我们会在比萨中添加这种配料。
# prompt = "\n请输入披萨配料： "
# message = ""
# while True:
#     message = input(prompt)
#     if 'quit' == message:
#         break
#     else:
#         print("我们会在披萨中添加这种配料！")

# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；3~12 岁的观众为 10 美元；
# 超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。

# prompt = "\n请问你今年多大： "
# while True:
#     age_str = input(prompt)
#     if not str(age_str).isnumeric():
#         break
#     else:
#         age = int(age_str)
#         if age < 3:
#             print("free!")
#         elif age > 3 and age < 12:
#             print("10$")
#         else:
#             print("15$")


# prompt = "\n请问你今年多大： "
# flag = True
# while flag:
#     age_str = input(prompt)
#     if not str(age_str).isnumeric():
#         flag = False
#     else:
#         age = int(age_str)
#         if age < 3:
#             print("free!")
#         # elif age > 3 and age < 12:
#         elif 3 < age < 12:
#             print("10$")
#         else:
#             print("15$")


# 7-8 熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名
# 字；再创建一个名为 finished_sandwiches 的空列表。遍历列表 sandwich_orders，对于
# 其中的每种三明治，都打印一条消息，如 I made your tuna sandwich，并将其移到列表
# finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['三明治1', '三明治2', '三明治3']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("I made your tuna sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

# 7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习 7-8 而创建的列表
# sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样
# 的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个 while 循环将
# 列表 sandwich_orders 中的'pastrami'都删除。确认最终的列表 finished_sandwiches 中
# 不包含'pastrami'

sandwich_orders = ['11', 'pastrami', '22', '33', 'pastrami', '44', 'pastrami']
finished_sandwiches = []

print("Pastrami has been sold out")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If
# you could visit one place in the world, where would you go?”的提示，并编写一个打印调
# 查结果的代码块。
responses = {}
polling_active = True
while polling_active:
    name = input("\n What's u name?")
    place = input("\nIf you could visit one place in the world, where would you go?")
    responses[name] = place
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, pl in responses.items():
    print(name + " would like to visit " + pl + ".")
