# Чтобы не портить логику решния, будем считать что на ресепшн или митинг рум оргтехника отправляется только со склада :)
# Если на складе нет, то об этом сообщается пользователю

class Stock:
    def __init__(self):
        self.equip_in_stock ={}

    def in_stock(self, name, pc):
        if name in self.equip_in_stock.keys():
            self.equip_in_stock[name] += pc
        else:
            self.equip_in_stock[name] = pc


class Reception:
    def __init__(self):
        self.equip_in_recep ={}

    def in_reception(self, name, pc):
        if name in stock.equip_in_stock and stock.equip_in_stock[name] >= pc:
            stock.equip_in_stock[name] = int(stock.equip_in_stock[name]) - pc
        else:
            print(f'На складе нет такого количества {name}-ов, зайдите в другой раз')
            pc = 0
        if name in self.equip_in_recep.keys():
            self.equip_in_recep[name] += pc
        else:
            self.equip_in_recep[name] = pc


class MeetingRoom:
    def __init__(self):
        self.equip_in_meeting_r = {}

    def in_meeting(self, name, pc):
        if name in stock.equip_in_stock and stock.equip_in_stock[name] >= pc:
            stock.equip_in_stock[name] = int(stock.equip_in_stock[name]) - pc
        else:
            print(f'На складе нет такого количества {name}-ов, зайдите в другой раз')
            pc = 0
        if name in self.equip_in_meeting_r.keys():
            self.equip_in_meeting_r[name] += pc
        else:
            self.equip_in_meeting_r[name] = pc


class OfficeEqip:

    def __init__(self, name, color, if_works = True):
        self.color = color
        self.if_works = if_works
        self.name = name



    def to_stock(self, stock, pc, name):
        if pc > 0 and name in ['scanner', 'printer', 'xerox']:
            stock.in_stock(name, pc)
        else:
            print('Данные некорректны!')


    def to_reception(self, reception, pc, name):
        if pc > 0 and name in ['scanner', 'printer', 'xerox']:
            reception.in_reception(name, pc)
        else:
            print('Данные некорректны!')


    def to_meeting_r(self, meeting_r, pc, name):
        if pc > 0 and name in ['scanner', 'printer', 'xerox']:
            meeting_r.in_meeting(name, pc)
        else:
            print('Данные некорректны!')

class Printer(OfficeEqip):

    def __init__(self, ink, name, color, if_works = True):
        super().__init__(name, color, if_works)
        self.ink = ink


class Scanner(OfficeEqip):
    def __init__(self, brand, name, color, if_works = True):
        super().__init__(name, color, if_works)
        self.brand = brand


class Xerox(OfficeEqip):
    def __init__(self, name, size, color, if_works = True):
        super().__init__(name, color, if_works)
        self.size = size


printers = Printer('black', 'printer', 'grey')
stock = Stock()
meeting_r = MeetingRoom()
reception = Reception()

scanner = Scanner('HP', 'scanner', 'blue', False)
xerox = Xerox('xerox', 'small', 'red')

printers.to_stock(stock, 10, 'printer')
scanner.to_stock(stock, 10, 'scanner')
print(stock.equip_in_stock)

printers.to_meeting_r(meeting_r, 1, 'printer')
xerox.to_meeting_r(meeting_r, 6, 'xerox')
print(meeting_r.equip_in_meeting_r)

scanner.to_reception(reception, 5, 'scanner')
xerox.to_reception(reception, 1, 'xerox')
print(reception.equip_in_recep)

print(stock.equip_in_stock)