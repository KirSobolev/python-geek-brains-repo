def add_sep(sep, len):
    print('Конец задания')
    print(sep * len)

a = 'Hello world'
b = int(input('Tell me your lucky number!'))
c = input('What is your name?')

print(a)
print(f'Greetings, {c}!')
print(f"It is {b} degrees outside, isn't it?")

add_sep('-', 100)

time_inp = int(input('Введите время в секундах'))
if time_inp <= 86400:
    hours = time_inp // 3600
    minutes = time_inp // 60 - hours * 60
    seconds = time_inp % 60

    hours_str = str(hours)
    minutes_str = str(minutes)
    seconds_str = str(seconds)

    print(f'{hours_str.zfill(2)}:{minutes_str.zfill(2)}:{seconds_str.zfill(2)}')

else:
    print('Введенное Вами время больше чем 24 часа, а потому не помещается в часы. Вернее могло бы поместится,'
          'но выглядело бы убого'
          ';)')

add_sep('-', 100)

n = input('Введите ваше счастливое число')

print(f'Сумма Вашего числа n по формуле n+nn+nnn составляет: {int(n) + int(n+n) + int(n+n+n)}')


add_sep('-', 100)

number_inp_4 = int(input('Введите целое положительное число: '))

biggest_number = number_inp_4 % 10
number_inp_4 = number_inp_4 // 10

while number_inp_4 > 0:
    if number_inp_4 % 10 > biggest_number:
        biggest_number = number_inp_4 % 10
    number_inp_4 = number_inp_4 // 10
print(f'Наибольшая цифра из числа это: {biggest_number}')

add_sep('-', 100)

debit = int(input('Введите значение выручки Вашего предприятия'))
credit = int(input('Введите количество издержек Вашего предприятия'))

finance_result = debit - credit

if finance_result > 0:
    print('Поздравляем! Ваш бизнес прибылен!')
    profitability = debit / credit
    print(f'Рентабельность вашего бизнеса составляет: {profitability}')
    employee = int(input('Введите количество Ваших сотрудников'))
    profit_per_face = (debit - credit) / employee
    print(f'Чистая прибыль в пересчете на каждого работника Вашего прдеприятия составляет {profit_per_face}')
elif finance_result == 0:
    print('Ваше предприятие не приносит никакой прибыли. С другой стороны и издержек тоже.'
          'Необходима оптимизация.')
else:
    print('От вашего предприятия одни убытки')

add_sep('-', 100)

result_1 = int(input('Результат на 1-ый день: '))
result_final = int(input('Желаемый результат: '))
day_cnt = 1

while result_1 < result_final:
    result_1 = result_1 + result_1 / 10
    day_cnt += 1
1
print(f'Атлет достигнет результата {result_final}км за {day_cnt} дней')

add_sep('-', 100)