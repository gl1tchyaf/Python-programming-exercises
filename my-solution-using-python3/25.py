'''Define a class, which have a class parameter and have a same instance parameter.'''

class Person:
    name = "Person"
    age = 0

    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age


jeffrey = Person("Jeffrey", 25)
print("%s name is %s and age is %d" % (Person.name, jeffrey.name, jeffrey.age))

nico = Person()
nico.name = "Nico"
nico.age = 25
print("%s name is %s and age is %d" % (Person.name, nico.name, nico.age))