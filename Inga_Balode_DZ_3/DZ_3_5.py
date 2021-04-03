# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice, shuffle
from itertools import islice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


#Могут быть повторения
def get_jokes_recur(lenght):
    result =[]
    while len(result) < lenght:
            noun = choice(nouns)
            adv = choice(adverbs)
            adj = choice(adjectives)
            joke = f'{noun} {adv} {adj}'
            result.append(joke)
    print(result)


get_jokes_recur(2)


#Повторений быть не может


jokes_result = []
def get_jokes(lenght):
    """
    Creates random struings from the nouns, adverbs, adjectives lists without the recurrences.

    :param lenght: int
    :return: strings created from the list items
    """
    for jokes in islice(zip(nouns, adverbs, adjectives), lenght):
        shuffle(nouns)
        shuffle(adjectives)
        shuffle(adverbs)
        jokes = ' '.join(jokes)
        jokes_result.append(jokes)
    print(jokes_result)

get_jokes(3)