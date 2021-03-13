"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNumeral:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumeral(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumeral((self.a * other.a - self.b * other.b), (self.a * other.b +  self.b * other.a))

    def __str__(self):
        return f'x = {self.a}, {self.b}'


x_1 = ComplexNumeral(1, 20)
x_2 = ComplexNumeral(5, 7)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)