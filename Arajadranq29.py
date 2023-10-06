from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @ abstractmethod
    def __init__(self):
        pass


    @ abstractmethod
    def perimeter(self):
        pass
    @ abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        if r >= 0:
            self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)

class Rectangle(Shape):
    def __init__(self, l, e):
        if l >= 0 and e >= 0:
            self.l = l
            self.e = e

    def perimeter(self):
        return 2 * (self.l * self.e)

    def area(self):
        return self.l * self.e


class Triangle(Shape):
    def __init__(self, a = None, b = None, c = None, alp = None, r = None, h = None):
        if c is None:
            c = 0.5 ** (((a ** 2 + b ** 2) - 2 * a * b) * math.cos(alp))
        elif a is None:
            a = 0.5 ** (((c ** 2 + b ** 2) - 2 * c * b) * math.cos(alp))
        elif b is None:
            b = 0.5 ** (((a ** 2 + c ** 2) - 2 * a * c) * math.cos(alp))
        if not a is None and not b is None and not c is None:
            if a + b > c and a + c > b and b + c > a:
                self.a = a
                self.b = b
                self.c = c
                self.alp = alp
                self.r = r
                self.h = h


    def perimeter(self):
        return  (self.a + self.b + self.c)


    def area(self):
        if not self.h is None:
            return self.a * (self.h **2)
        elif self.h is None and not self.alp is None:
            return self.a * self.b * math.sin(self.alp)
        else:
            return ((self.perimeter() * 0.5) * ((self.perimeter() * 0.5) - self.a) * ((self.perimeter() * 0.5) - self.b) * ((self.perimeter() * 0.5) - self.c)) ** 0.5




f1 = Triangle(5,4, 6, 4, 5, 5)
print(f1.area())

f2 = Circle(5)
print(f2.perimeter())


