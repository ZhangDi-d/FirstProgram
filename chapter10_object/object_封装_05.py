# coding:utf-8

'''

'''


class Person(object):
    def __hello(self, data):
        print(f' hello{data}')

    def helloworld(self):
        self.__hello('world')


if __name__ == '__main__':
    person = Person()
    person.helloworld()
