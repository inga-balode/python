# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
#
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


# НЕ оптимизированное
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = [n for n in src if src.count(n)==1]
print(unique_src)

# оптимизированное
unique_src_2 = set()
x = set()
for n in src:
    if n not in x:
        unique_src_2.add(n)
    else:
        unique_src_2.discard(n)
    x.add(n)

unique_src_ord = [n for n in src if n in unique_src_2]
print(unique_src_ord)

