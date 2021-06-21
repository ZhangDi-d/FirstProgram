# coding:utf-8
"""
序列化

class set def 不可以进行序列化

json ，pickle
"""
import json
import pickle

result = json.dumps([1, 2])
print(result)

a = {'name': '张三'}
a_json = json.dumps(a)
print(a_json)

print(json.loads(result))
print(json.loads(a_json))

none_json = json.dumps(None)
print(none_json)

print(json.loads(none_json))


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    return json.loads(data)


def write(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError("data is dict")


data = {'name': "zhangsan", 'age': 20}

if __name__ == "__main__":
    #write('test_serial.json', data)
    result = read('test_serial.json')
    print(result)
