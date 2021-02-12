"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

seasons = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

users_number = int(input('Введите число от 1 до 12'))

# key_list = list(seasons.keys())
# values_list = sum(list(seasons.values()), [])
# index = values_list.index(users_number) // 3
# print(key_list[index])

print(list(seasons.keys())[sum(list(seasons.values()), []).index(users_number) // 3])
