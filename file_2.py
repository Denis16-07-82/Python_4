# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
# формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз меньше объема ОЗУ
import json

with open('users.csv', 'r', encoding='utf-8') as users:
    users_list = []
    for ln in users:
        users_list.append(' '.join(ln.split()[0].split(',')))
    print(users_list)
    users_dict = {}.fromkeys(users_list)
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    # for ln, lm in zip(hobby, users_list):
    #     users_dict[lm] = ' '.join(ln.split())
    hobby_list = []
    for ln in hobby:
        hobby_list.append(' '.join(ln.split()))
    if len(users_list) >= len(hobby_list):
        for lm, ln in zip(users_list, hobby_list):
            users_dict[lm] = ln
        print(users_dict)
        with open('users_dict.json', 'w', encoding='utf-8') as dict_file:
            json.dump(users_dict, dict_file)
        with open('users_dict.json', 'r', encoding='utf-8') as dict_file:
            users_dict = json.load(dict_file)
            print(users_dict)
    else:
        print(f'Код ошибки {1}')
