"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    sort_list = sorted([a, b, c])
    return sort_list[-1] + sort_list[-2]


print(my_func(123, 0, 7))
