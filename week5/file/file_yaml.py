# coding:utf-8

"""
yaml PyYAML-5.4.1
"""
import yaml


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)
    return result


if __name__ == '__main__':
    result = read('test.yaml')
    print(result)
