"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""
from itertools import cycle
from time import sleep


class TrafficLight:
    color_states = {'red': 7,
                    'yellow': 2,
                    'green': 7}

    def __init__(self, color=None):
        self.__color = color

    def turn_on(self, counter):
        for color, time in cycle(self.color_states.items()):
            if counter <= 0:
                break
            self.__color = color
            print(f'Color has been changed to {color} for {time} seconds')
            sleep(time)
            counter -= 1


tr_light = TrafficLight('red')
tr_light.turn_on(6)
