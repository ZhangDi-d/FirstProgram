# coding:utf-8

"""
re1|re2  或者
^ 开头  \A
$ 结尾   \Z
.
*
{N}
{M-N}
\ 转义
"""
import re

data = '122@gmail.com'
print(re.findall('gmail|com', data))
print(re.findall('^122', data))
print(re.findall('com$', data))
print(re.findall('\w*', data))
print(re.findall('\w+', data))  # 至少匹配一次
print(re.findall('\w{3}', data))  # 匹配3个
print(re.findall('[a-z]{3}', data))  # 匹配3个
print(re.findall('\w{1,}', data))  #
print(re.findall('[^122]', data))  # [^...] 过滤

## 组的概念 ，从1开始
test = 'hello, my name is lisi'
result = re.search('hello, (.*) name is (.*)', test)
print(result.group())
print(result.group(1))


