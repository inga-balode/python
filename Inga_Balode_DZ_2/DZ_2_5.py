# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# Задачи с ** предназначены для продвинутых учеников, которым мало сделать обычное задание.

prices_lst = [57.8, 46.51, 97, 45.67, 89.04, 78, 63.99, 82.21, 67, 29 , 22]



result = []
for i in prices_lst:
    i = "%.2f" % i
    rub, kk = i.split('.')
    str_pr = f'{rub} руб. {kk} коп. '
    result += [str_pr]

result_str = ', '.join(result)
print(result_str)


print(id(prices_lst))
prices_lst.sort()
print(prices_lst)
print(id(prices_lst))

prices_lst.reverse()
print(prices_lst)

high_prices = prices_lst[:5:1]
print(list(reversed(high_prices)))
