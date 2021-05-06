class InputError(Exception):

    def __init__(self, txt):
        self.txt = txt

result = []

try:
    while True:
        number = input('Введите число:')
        if number.isnumeric() and number != 'stop':
            result.append(number)
        elif number == 'stop':
            print(result)
            break
        elif number.isnumeric()==False:
            raise InputError('Это не число!')
except InputError as e:
        print(e.txt)





