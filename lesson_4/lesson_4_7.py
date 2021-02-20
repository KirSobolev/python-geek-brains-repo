"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""
from math import factorial


def fact_v1(n):
    for number in range(1, n + 1):
        if number != 1:
            yield factorial(number)
        else:
            yield number


for el in fact_v1(4):
    print(el)


def fact_v2(num):
    factor = 1
    for el in range (1, num + 1):
        factor *= el
        yield factor


for el in fact_v2(4):
    print(el)