#Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

perc = "процент"
for i in range(0,21):
    if i == 1 :
        print(str(i) + " " + perc)
    elif i >= 2 and i <5:
        print(str(i) + " " + perc + "a")
    else:
        print(str(i) + " " + perc + "ов")

