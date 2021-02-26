"""Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

firms_plus = {}
firms_minus = {}
avg = {'average_profit': None}
result = [firms_plus, avg]

with open('task_7.txt', 'r') as task_7_file:
    max_len = len(task_7_file.readlines())
    task_7_file.seek(0)
    for cnt in range(0, max_len):
        content = task_7_file.readline().split()
        if int(content[-1]) < int(content[-2]):
            firms_plus[content[0]] = int(content[-2]) - int(content[-1])
            avg['average_profit'] = sum(firms_plus.values()) / len(firms_plus)
        else:
            firms_minus[content[0]] = int(content[-1]) - int(content[-2])
print(f'фирмы, вышедшие в плюс: {firms_plus}, их средняя прибыль составляет {avg}.\n'
      f'Фирмы, оставшиеся в минусе: {firms_minus}\n')
with open('result_task_7.json', 'w') as result_save:
    json.dump(result, result_save)
print('Данные сохранены.')
