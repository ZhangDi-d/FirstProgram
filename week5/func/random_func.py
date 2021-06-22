# coding:utf-8
import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))
print(random.choice('abc'))

print(random.sample(['a', 'b', 'c'], 2))
print(random.sample('abc', 2))

print(random.randrange(1, 10, 2))
