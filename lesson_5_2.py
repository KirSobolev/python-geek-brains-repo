"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open("task_2.txt", 'r') as task_2_file:
    strings_cnt = len(task_2_file.readlines())
    task_2_file.seek(0)
    words_cnt = len(task_2_file.read().split())
    print(f'There are {strings_cnt} strings and {words_cnt} words in {task_2_file.name}')
