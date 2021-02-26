"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

salary_list = []

d = {}

with open('task_3.txt', 'r') as task_3_file:
    string_brakes_replaced = task_3_file.read().replace('\n', ' - ')

source_list = string_brakes_replaced.split(' - ')

for value in range(1, len(source_list), 2):
    salary_list.append(int(source_list[value]))
for k in range(0, len(source_list), 2):
    d[source_list[k]] = int(source_list[k+1])
for i in d:
    if d[i] < 20000:
        print(f'Attention! {i} is underpaid!')

avg_salary = sum(salary_list) / len(salary_list)
print(f'Average salary is {avg_salary}')
