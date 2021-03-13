"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка."""


class OnlyNumerals(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        el = input('Введите ваше число, для выхода введите "stop"')
        if el.lower() == 'stop':
            break
        if not el.isdigit():
            raise OnlyNumerals('Введено НЕ число!')
        my_list.append(el)
    except OnlyNumerals as err:
        print(err)
print(my_list)