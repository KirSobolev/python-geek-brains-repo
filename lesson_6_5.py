"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    title = 'Mother of others'

    def draw(self):
        return f'{self.title}, Запуск отрисовки'


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return f'{self.title}, Я ручка ручка ручка, а вовсе не медведь'


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return f'{self.title}, на три буквы длинее ручки'


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return f'{self.title}, как ручка только толще'


mother = Stationery()
pen = Pen()
pencil = Pencil()
h = Handle()

print(mother.draw())
print(pen.draw())
print(pencil.draw())
print(h.draw())
