"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
values = []
d = {}
with open('task_6.txt', 'r', encoding='UTF-8') as task_6_file:
    max_strings = len(task_6_file.readlines())
    task_6_file.seek(0)
    for cnt in range(0, max_strings):
        content = task_6_file.readline().replace('-', '0').split(': ')
        for i in content[1]:
            if i.isdigit() or i == ' ':
                values.append(i)
        values = ''.join(values)
        values = values.split()
        for el in range(0, len(values)):
            values[el] = int(values[el])
        d[content[0]] = sum(values)
        values = []
print(d)





