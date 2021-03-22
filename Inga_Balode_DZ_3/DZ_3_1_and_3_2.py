# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

#print(user_5.get('address'))  # None
# print(user_5.get('address', 'адрес не задан'))  # адрес не задан

en_ru_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять' }


def num_translate(word):
    print(en_ru_dict.get(word))


num_translate("six")
num_translate("zero")
num_translate("eleven")


# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate_adv(word):
    if word[0].isupper() == True:
        word = word.lower()
        result = en_ru_dict.get(word)
        print(result.capitalize())
    else:
        print(en_ru_dict.get(word))



num_translate_adv("One")
num_translate_adv("zero")
num_translate_adv("eleven")


