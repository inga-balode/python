import numpy

class ComplexNumber:


    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)


    def __mul__(self, other):
        a = self.real
        b = self.imag
        c = other.real
        d = other.imag
        return ComplexNumber(a*c - b*d, b*c + a*d)


    def __str__(self):
        return f'{self.real} + {self.imag}i'


complex_1 = ComplexNumber(1, 3)
complex_2 = ComplexNumber(2, 4)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
