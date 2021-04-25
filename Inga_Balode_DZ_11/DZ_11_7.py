import numpy

class ComplexNumber:


    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        i = numpy.lib.scimath.sqrt(-1)
        x = (self.real + self.imag * i) + (other.real + other.imag * i)
        return x

    def __mul__(self, other):
        i = numpy.lib.scimath.sqrt(-1)
        x = (self.real + self.imag * i) * (other.real + other.imag * i)
        return x


complex_1 = ComplexNumber(1, 3)
complex_2 = ComplexNumber(2, 4)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
