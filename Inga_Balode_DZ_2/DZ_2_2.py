# 2. Дан список:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# 3. ** (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

numbers = list(range(0, 10))

numbers_str = []
for i in numbers:
    i = str(i)
    numbers_str += i


result = []
for i in start_list:
    if i[-1] in numbers_str:
        if i[0] in "+-":
            sign = i[0]
            i = i[1:]
            i = int(i)
            str_temp = f"'{sign} {i:02}'"
            result += [str_temp]
        else:
            i = int(i)
            str_i = f"'{i:02}'"
            result += [str_i]
    else:
        result += [i]

result_str = ' '.join(result)
print(result_str)
