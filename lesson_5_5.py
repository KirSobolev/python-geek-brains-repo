"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open('task_5.txt', 'w') as task_5_file:
    task_5_file.write(input('Type numerals here using "Space" as a separator: '))

with open('task_5.txt', 'r') as task_5_file_sum:
    numbers_list = task_5_file_sum.read().split()

for number in range(0, len(numbers_list)):
    numbers_list[number] = int(numbers_list[number])

res = sum(numbers_list)
print(f'Sum of your numerals is {res}')