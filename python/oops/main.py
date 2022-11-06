x = 1
print(type(x))


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print("bark")


d = Dog("one", "pink")


# print(d.name, d.color)


class Person:
    count = 1

    @classmethod
    def number_of_people(cls):
        return cls.count


# print(Person.number_of_people())

class Student:
    __schoolName = "Dal"

    def __init__(self, name, age):
        self._age = age
        self.__name = name


s = Student("abhi", 10)
print(s.__name)
