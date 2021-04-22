# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color


    def running(self):
        print('Поехали')

    def light_color(self):
        while True:
            color = 'red'
            print(color)
            sleep(7)
            color = 'yellow'
            print(color)
            sleep(2)
            color = 'green'
            print(color)
            sleep(10)

traffic_light_1 = TrafficLight(color='red')
# print(traffic_light_1.color)


traffic_light_1.light_color()