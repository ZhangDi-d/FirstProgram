# coding : utf-8

class Tool(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'


class Food(object):
    def work(self):
        return 'food work'

    def cake(self):
        return 'food cake'


class Person(Tool, Food):
    pass


if __name__ == '__main__':
    p = Person()
    car = p.car()
    cake = p.cake()
    print(car)
    print(cake)

    work = p.work()
    print(work)

    print(Person.__mro__)
