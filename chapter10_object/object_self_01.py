# coding:utf-8

class Person(object):
    name = None
    age = None

    def run(self):
        print("%s run" % self.name)

    def jump(self):
        print("%s jump" % self.name)


person = Person()
person.run()
person.jump()

person1 = Person()
person1.name = "libai"  # self 类实例
person1.run()
person1.jump()

person1.weight = 60

print(person1.weight)

print(person.weight)  # 'Person' chapter10_object has no attribute 'weight'
