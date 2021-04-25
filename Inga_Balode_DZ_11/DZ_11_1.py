class Date:

    def __init__(self, event):
        self.event = event

    @staticmethod
    def get_date(value):
        day, month, year = value.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        print(day, month, year)

    @classmethod
    def get_valid_date(cls, param):
        day, month, year = param.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        if 0 < day < 31 and 0 < month <= 12 and year>=1:
            print(f'Дата: {day}-ое число {month} мес. {year} год')
        else:
            print('Дата некорректна')


Date.get_date('11-09-1875')

date_1 = Date('Birthday')
date_1.get_valid_date('12-10-1993')

