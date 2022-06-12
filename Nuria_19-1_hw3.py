# реализовать операцию над дробью, то есть создать класс Fraction
# у него будет 2 атрибута (numertor, denumerator)
# сделать add, sub, mul, floordiv (Dunder Methods)
# по правилам математики!)


class Fraction:

    def __init__(self, numerator, denumerator):
        self.num = numerator
        self.den = denumerator

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __mul__(self, otherFraction):
        newnum = self.num * otherFraction.num
        newden = self.den * otherFraction.den
        return Fraction(newnum, newden)

    def __add__(self, otherFraction):
        newnum = self.num * otherFraction.den + self.den * otherFraction.num
        newden = self.den * otherFraction.den
        return Fraction(newnum, newden)

    def __sub__(self, otherFraction):
        newnum = self.num * otherFraction.den - self.den * otherFraction.num
        newden = self.den * otherFraction.den
        return Fraction(newnum, newden)

    def __floordiv__(self, otherFraction):
        newnum = self.num * otherFraction.den
        newden = self.den * otherFraction.num
        return Fraction(newnum, newden)


a = Fraction(1, 2)
b = Fraction(2, 3)

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} // {} = {}'.format(a, b, a // b))





