class getError(Exception):

    def __init__(self, txt):
        self.txt = txt

a = input('Какое число хотите поделить?')
b = input('На какое число произведём деление?')

try:
    a = int(a)
    b = int(b)
    if b != 0:
        c = a / b
        print(int(c))
    else:
        raise getError('Деление на 0 невозможно!')
except getError as err:
    print(err.txt)


