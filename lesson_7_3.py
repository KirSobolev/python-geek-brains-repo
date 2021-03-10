"""Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно."""


class Cell:
    def __init__(self, quantity_of_inner_cells):
        self.quantity = quantity_of_inner_cells

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if abs(self.quantity) != abs(other.quantity):
            return self.quantity - other.quantity if self.quantity > other.quantity else other.quantity - self.quantity
        else:
            return f'Клетки одинаковы! Вычитание невозможно'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity if self.quantity > other.quantity else other.quantity // self.quantity

    def make_order(self, max_cells_in_row):
        full_rows = self.quantity // max_cells_in_row
        last_row = self.quantity % max_cells_in_row
        return '\n'.join(['*' * max_cells_in_row] * full_rows + (['*' * last_row]))



cell_a = Cell(12)
cell_b = Cell(25)

print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a * cell_b)
print(cell_a / cell_b)
print(cell_a.make_order(5))


