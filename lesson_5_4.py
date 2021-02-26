"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

d = {'One': 'Один',
     'Two': 'Два',
     'Three': 'Три',
     'Four': 'Четыре'}

with open('task_4.txt', 'r') as task_4_file:
    source = task_4_file.read().replace('\n', '  - ').split(' - ')


for i in range(0, len(source), 2):
    source[i] = d[source[i]]

res = ' - '.join(source).replace('  - ', '\n')
print(res)

with open('task_4_ru.txt', 'w', encoding='UTF-8') as task_4_file_ru:
    task_4_file_ru.write(res)
