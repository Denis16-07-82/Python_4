# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
# список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


with open(r'C:\Users\User\Desktop\nginx_logs.txt', 'r', encoding='utf-8') as my_file:
    block = my_file.readlines(10 ** 6)
    my_list = []
    my_list_new = []
    while block:
        for ln in block:
            my_tuple = (ln.split('"')[0].split()[0],
                        ln.split('"')[1].split()[0],
                        ln.split('"')[1].split()[1])
            my_list.append(my_tuple)
            my_list_new.append(ln.split('"')[0].split()[0])
        block = my_file.readlines(10 ** 6)
    print(my_list[0],my_list[1],my_list[2])
    my_set = frozenset(my_list_new)
    my_max = max([my_list_new.count(lm) for lm in my_set])
    print(my_max)
    for ln in my_set:
        if my_list_new.count(ln)==my_max:
            print(f'Спамер:{ln}')
            break




