from abc import ABC, abstractmethod

class Clothes:

    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calc(self):
        count = self.size/6.5 + 0.5
        return count

class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def calc(self):
        count = 2 * self.height + 0.3
        return count

my_coat = Coat(34)
print(my_coat.calc)

my_suit = Suit(175)
print(my_suit.calc)