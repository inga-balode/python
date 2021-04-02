# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_nums(n):
    for i in range(1, int(n)+1):
        if i%2 != 0:
            yield i

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

n = input('Введите число: ')
result = (x for x in range(1, int(n)+1) if x%2 != 0)
print(next(result))
print(next(result))
print(next(result))
print(next(result))




