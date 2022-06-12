# реализовать операцию над дробью, то есть создать класс Fraction
# у него будет 2 атрибута (numertor, denumerator)
# сделать add, sub, mul, floordiv (Dunder Methods)
# по правилам математики!)


class Fraction:

    def __init__(self, numerator, denumerator):
        self.num = numerator
        self.den = denumerator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __floordiv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)


a = Fraction(4, 5)
b = Fraction(2, 3)

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} // {} = {}'.format(a, b, a // b))





