"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""


class MyZeroDivisionError(Exception):
    def __init__(self, txt='Деление на ноль!'):
        self.txt = txt


def div_func(a, b):
    if b == 0:
        raise MyZeroDivisionError('Деление на ноль невозомжно!')
    return a / b


try:
    print(div_func(10, 0))
except MyZeroDivisionError as err:
    print(err)
