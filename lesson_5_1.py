"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("task_1.txt", 'w') as task_1_file:
    while True:
        user_input = input('Input empty string to exit\nType your text here: ')
        if user_input == '':
            print('Thank you for using our services')
            break
        task_1_file.write(f'{user_input}\n')