"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        return f'What does the car say? Vivivivivivivivivi!'

    def stop(self):
        return f'Car stopped'

    def turn(self, direction):
        ways = {'left': 'Car is turning to the left',
                'right': 'Car is turning to the right',
                'u_turn': 'Car made U-turn'}
        return f'{ways[direction]}'

    def show_speed(self):
        return f'Your speed - {self.speed}'

    def get_full_info(self):
        return f'Max speed - {self.speed}, car color - {self.color}, car name - {self.name}'


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return f'Remember 60 kmh speed limit!!!'
        else:
            return f'Your speed is {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return f'Remember 40 kmh speed limit!!!'
        else:
            return f'Your speed is {self.speed}'


class PoliceCar(Car):
    pass


t_car_1 = TownCar(70, 'red', 'Ford Focus')
print(t_car_1.go())
print(t_car_1.stop())
print(t_car_1.turn('left'))
print(t_car_1.show_speed())
print(t_car_1.get_full_info())

t_car_2 = TownCar(50, 'blue', 'Ford Mondeo')
print(t_car_1.show_speed())
print(t_car_1.get_full_info())

w_car_1 = WorkCar(49, 'red', 'Ford Transporter')
print(w_car_1.show_speed())
print(w_car_1.get_full_info())

