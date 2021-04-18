import math


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


c = Circle(10)
print(c.area())
print(type(c))

assert type(c) == Circle

a = 5  # 5 is an object
b = {'x': 5, 'y': 3}  # dicts are objects
c = "hello"  # strings are objects too
d = c  # two variables sharing an object
e = c.lower()  # should generate a new object
f = 8 * b['y'] - 19  # what happens here?  --> 8 * 3 - 19

for obj in (a, b, b['x'], b['y'], c, d, e, f):
    print(id(obj))


class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

    def speak(self):
        return f"{self.name} says {self.sound()}"


class Cow(Animal):
    def sound(self):
        return "moooo"


class Horse(Animal):
    def sound(self):
        return "neigh"


class Sheep(Animal):
    def sound(self):
        return "baaaa"


if __name__ == "__main__":
    s = Horse("CJ")
    print(s.speak())
    print(Sheep("Little lamb").speak())

