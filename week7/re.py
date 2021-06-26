# coding:utf-8
"""
search

match

findall

groups

\A 开头
\Z 结尾
\d  数字
\D  非数字
\w 字母数字等符号
\W 非字母
"""

import re

str_data = 'hello world,this is a good day'
result = re.search('h([a-z])s', str_data)
print(result.groups())


def had_number(data):
    result = re.findall('\d', data)
    if len(result) == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    result = had_number('12  tt')
    print(result)
