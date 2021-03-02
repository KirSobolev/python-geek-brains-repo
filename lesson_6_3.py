"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данныe,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    _salary = {'director': {'wage': 100000, 'bonus': 5000},
              'dvornik': {'wage': 1000, 'bonus': 50},
              'manager': {'wage': 30000, 'bonus': 3000}}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self._salary[position]['wage'] + self._salary[position]['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_full_income(self):
        return f'Total income: {self._income}'


worker_1 = Position('Ivan', 'Ivanov', 'director')
worker_2 = Position('Egor', 'Egorov', 'dvornik')
worker_3 = Position('Petr', 'Petrov', 'manager')

print(worker_1.get_full_name())
print(worker_1.get_full_income())
print(worker_2.get_full_name())
print(worker_2.get_full_income())
print(worker_3.get_full_name())
print(worker_3.get_full_income())