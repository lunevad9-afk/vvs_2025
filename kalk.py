
import math

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Ошибка: Деление на ноль"
        return x / y

    def sin(self, degrees):
        radians = math.radians(degrees)
        return math.sin(radians)

    def cos(self, degrees):
        radians = math.radians(degrees)
        return math.cos(radians)

    def tan(self, degrees):
        radians = math.radians(degrees)
        return math.tan(radians)

    def log(self, x, base=10):
        if x <= 0:
            return "Ошибка: Логарифм отрицательного числа"
        return math.log(x, base)

    def power(self, base, exponent):
        return math.pow(base, exponent)
        
print(Calculator().log(9,3))
