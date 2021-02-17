"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def contact_info_version_1(name, surname, year_birth, city, email, phone_number):
    print(f'Гражданин {name.capitalize()} {surname.capitalize()}, {year_birth} года рождения, проживающий(ая) в городе:'
          f'{city.capitalize()}, контактные данные: {email}, {phone_number}')


def contact_info_version_2(**kwargs):
    return kwargs


contact_info_version_1(name='имя', surname='фамилия', year_birth=9999, city='город', email='электронная почта',
                       phone_number='номер телефона')

contact = contact_info_version_2(name='имя'.capitalize(), surname='фамилия'.capitalize(), birthday=9999,
                                 city='город'.capitalize(), email='электронная почта', phone_number='номер телефона')
print(str(contact))

