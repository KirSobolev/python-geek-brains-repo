"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_int(cls, date: "Data"):
        return list(map(int, date.date_string.split('-')))

    @staticmethod
    def is_date_valid(date: "Data"):
        print('Запускаем процесс валидации указанной даты')
        source_date = date.date_string.split('-')
        if not 0 < int(source_date[1]) < 13:
            raise ValueError('Месяц указан неверно!')
        if not 0 < int(source_date[0]) < 32:
            raise ValueError('День указан неправильно!')
        print('Процесс валидации завершен успешно')


x = Data('17-07-1889')
x.is_date_valid(x)
print(Data.date_int(x))
