"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class ParentCloth(ABC):
    @abstractmethod
    def cloth_calc(self):
        ...


class Coat(ParentCloth):
    def __init__(self, V):
        self.size = V

    @property
    def cloth_calc(self):
        return self.size / 6.5 + 0.5


class Suit(ParentCloth):
    def __init__(self, H):
        self.size = H

    @property
    def cloth_calc(self):
        return self.size / 6.5 + 0.5


def total_cloth_calc(cloth_1, cloth_2):
    result = cloth_1 + cloth_2
    print(f'Для пошива и пальто и костюма потребуется {str(result)[0:4]} метров ткани')
    return result


my_coat = Coat(5)
my_suit = Suit(10)

total_cloth_calc(my_coat.cloth_calc, my_suit.cloth_calc)