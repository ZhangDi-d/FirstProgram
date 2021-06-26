# coding:utf-8

# 贪婪与非贪婪  ： 0或者多次属于贪婪模式  ？组合编程非贪婪
import re

url = 'http://www.baidu.com/'


def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w+\.\w+\.\w+/', url)
    if len(result) != 0:
        return True
    else:
        return False


def get_url(url):
    result = re.findall('http://(\w+\.*\w+\.\w+)', url)
    if len(result) != 0:
        return result[0]
    else:
        return ''

if __name__ == "__main__":
    result = check_url(url)
    print(result)

    result = get_url(url)
    print(result)
