"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        result = []
        try:
            if len(self.matrix) != len(other.matrix):
                raise ValueError(f'Remember that either matrices have to be exactly the same size!')
            for item in zip(self.matrix, other.matrix):
                result.append([sum([a, b]) for a, b in zip(*item)])
            return Matrix(result)
        except Exception as err:
            print(f'Error: {err}')


almost_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix = Matrix(almost_matrix)

almost_matrix_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
not_my_matrix = Matrix(almost_matrix_2)

print(my_matrix, '\n')
print(my_matrix + not_my_matrix)
