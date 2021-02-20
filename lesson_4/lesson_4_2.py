"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

list_start = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_result = [list_start[el] for el in range(1, len(list_start)) if list_start[el] > list_start[el - 1]]

print(f'Old list: {list_start}')
print(f'New list: {list_result}')