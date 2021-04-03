# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
#
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!

cubed_lst = []
for i in range(0, 1001):
    if i % 2 == 0:
        i = i ** 3
        cubed_lst.append(i)

print(cubed_lst)

sum = 0
result = 0
for a in cubed_lst:
    result = 0
    i = a
    while i > 0:
        digit = i % 10
        i = i // 10
        result += digit
    if result % 7 == 0:
        sum += a

print(sum)

#если с новым списком (сумма чисел с учетом прибавления 17)
new_cubed_list = []

for x in cubed_lst:
    x += 17
    new_cubed_list.append(x)

print(new_cubed_list)

new_summ = 0
result = 0
for x in new_cubed_list:
    result = 0
    i = x
    while i > 0:
        digit = i % 10
        i = i // 10
        result += digit
    if result % 7 == 0:
        new_summ += x


print(new_summ)


#не создавая список (сумма чисел с учетом прибавления 17)

n = 0
summ = 0
result = 0
while n < len(cubed_lst):
    cubed_lst[n] = int(cubed_lst[n]) + 17
    n +=1

# ИЛИ
# for id in range(len(cubed_lst)):
#     cubed_lst[id] += 17

for a in cubed_lst:
    result = 0
    i = a
    while i > 0:
        digit = i % 10
        i = i // 10
        result += digit
    if result % 7 == 0:
        summ += a

print(cubed_lst)
print(summ)


# сумма оригинальных чисел списка ( до прибавления 17)

n = 0
summ = 0
result = 0


for a in cubed_lst:
    x = a
    result = 0
    i = a + 17
    while i > 0:
        digit = i % 10
        i = i // 10
        result += digit
    if result % 7 == 0:
        summ += x


print(cubed_lst)
print(summ)


