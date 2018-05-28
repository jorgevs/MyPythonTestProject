# Class1 ===========================================================================

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Animal:
    __name = ""
    __height = 0
    __weight = 0

    # Constructor
    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight

    # Setters methods
    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    # Getters methods
    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_type(self):
        print("Animal")

    # Other methods
    def toString(self):
        return "{} is {} cm tall and {} kilograms".format(self.__name, self.get_height(), self.__weight)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


cat = Animal('Whiskers', 20, 12)
print(cat.toString())


# Inheritage
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms. His owner is {}".format(self.__name, self.get_height(),
                                                                           self.__weight, self.__owner)


dog = Dog("Buppys", 20, 20, "Ivis")


# Polymosrphism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(dog)


# Class2 ===========================================================================

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Talker(object):
    def greet(self, name):
        print('Hello, %s!' % name)

    def farewell(self, name):
        print('Farewell, %s!' % name)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


t = Talker()
t.greet("Jorge")
t.farewell("Jorge")
