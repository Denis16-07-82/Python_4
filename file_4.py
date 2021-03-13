# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    string_of_numbers = input('Введите через пробел два номера строк или без пробела один номер или нажмите Enter:')
    if len(string_of_numbers) == 0:
        sale_str = f.readline()
        while sale_str:
            print(f'Продажи булочной:{sale_str.strip()}')
            sale_str = f.readline()
    elif len(string_of_numbers.split()) == 2:
        for ln in range(min(int(string_of_numbers.split()[0]), int(string_of_numbers.split()[1])),
                        max(int(string_of_numbers.split()[0]), int(string_of_numbers.split()[1])) + 1):
            f.seek(14 * (ln - 1))
            sale_str = f.readline()
            if sale_str:
                print(f'Продажи булочной:{sale_str.strip()}')
            else:
                break
    elif len(string_of_numbers.split()) == 1:
        f.seek(14 * (int(string_of_numbers.split()[0]) - 1))
        sale_str = f.readline()
        while sale_str:
            print(f'Продажи булочной:{sale_str.strip()}')
            sale_str = f.readline()
    else:
        print('Вы некорректно ввели данные:введите не более двух чисел')
