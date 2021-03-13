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

for a in cubed_lst:
    a = int(a)
    if a % 7 == 0:
        while a > 0:
            digit = a % 10
            sum = sum + digit
            a = a // 10
print(sum)


#если с новым списком

new_cubed_list = []

for x in cubed_lst:
    x = int(x) + 17
    new_cubed_list.append(x)

new_summ = 0
for x in new_cubed_list:
    x = int(x)
    if x % 7 == 0:
        while x > 0:
            digit = x % 10
            new_summ = new_summ + digit
            x = x // 10

print(new_cubed_list)
print(new_summ)


#не создавая список


n = 0
summ = 0
while n < len(cubed_lst):
    cubed_lst[n] = int(cubed_lst[n]) + 17
    n +=1

# ИЛИ
# for id in range(len(cubed_lst)):
#     cubed_lst[id] += 17

for i in cubed_lst:
    i = int(i)
    if i % 7 == 0:
         while i > 0:
            new_digit = i % 10
            summ = summ + new_digit
            i = i // 10

print(cubed_lst)
print(summ)

