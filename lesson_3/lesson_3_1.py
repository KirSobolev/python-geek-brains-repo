"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def division(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return f'Знаменатель не может равнятся нулю, {ZeroDivisionError}'
    except TypeError:
        return f'Оба аргумента должны быть числами, {TypeError}'


print(division(1, 0))
print(division('Should i put some strings everywhere', 'Just for lulz'))
print(division(2, 2))