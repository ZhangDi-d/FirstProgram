# coding:utf-8

import os


def create_package(path):
    if os.path.exists(path):
        raise Exception('%s 已经存在了' % path)
    os.makedirs(path)

    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write("# coding:utf-8\n")
    f.close()


create_package(os.getcwd() + "/test")

# current_path = os.getcwd()
# print(current_path)
#
# f = open(current_path + "/a.txt", "w")
# f.write('hello world')
# f.close()
