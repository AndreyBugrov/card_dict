from random import randint


def get_key_and_value(cd: dict, need_None: bool):
    local_key = input("Фраза на английском: ")
    if local_key == 'q':
        print("Действие отменено")
        return None, None
    else:
        if need_None:
            if cd.get(local_key, None) is not None:
                raise KeyError('Такая фраза уже есть в словаре')
        else:
            if cd.get(local_key, None) is None:
                raise KeyError('Такой фразы нет в словаре')
    local_value = input("Переводы через запятую: ")
    if local_value == 'q':
        print("Действие отменено")
        return None, None
    print("Успех!")
    return local_key, local_value


print("Enter number of file: ")
s = ''
while s != '1' and s != '2' and s != 'q':
    s = input("1 - Технический словарь, 2 - Повседневный словарь, q - Выход\n")
    if s == '1':
        filename = "Технический Словарь.txt"
    else:
        if s == '2':
            filename = "Повседневный Словарь.txt"
        else:
            if s == 'q':
                print("До свидания!")
                exit(0)
card_dict = dict()  # Основной словарь
key_list = []
with open(filename, encoding='utf-8', newline="\n") as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        key = lines[i][:-2]
        key_list.append(lines[i][:-2])
        i += 1
        if i < len(lines):
            card_dict[key] = lines[i][:-2]
        i += 1
max_size = len(key_list) - 1  # Максимальный номер у английской фразы в списке
char = 'empty char'  # Вводимые символы
rand_key = key_list[randint(0, max_size)]
print('Чтобы посмотреть список команд, введите \"h\"')
print(rand_key)
while True:
    char = input("Ввод: ")
    if char == 'q':
        break
    elif char == 's':
        sorted_list_of_tuples = sorted(card_dict.items(), key=lambda x: x[0])
        card_dict = dict(sorted_list_of_tuples)
    elif char == 'a' or char == 'r':
        try:
            key, value = get_key_and_value(card_dict, char == 'a')
            if key is not None:
                card_dict[key] = value
                if char == 'a':
                    key_list.append(key)
                    max_size += 1
        except KeyError as ex:
            print(str(ex)[1:-1])
    elif char == 'd':
        key = input("Введите фразу на английском: ")
        try:
            card_dict.pop(key)
            key_list.remove(key)
            max_size -= 1
        except KeyError:
            print("Такой фразы нет в словаре")
    elif char == 'h':
        print('Команды:')
        print('q - выход из приложения')
        print('s - сортировка словаря')
        print('a - добавить значение в словарь')
        print('d - удалить значение из словаря')
        print('r - изменить перевод')
        print('h - список команд')
        print('c - сменить файл словаря')
        print('o - перенести изменения из словаря в файл')
        print('Любой иной набор символов - получение ответа (перевода на русский язык)')
    elif char == 'c':
        if s == 1:
            s = 2
            filename = "Повседневный Словарь.txt"
        else:
            s = 1
            filename = "Технический Словарь.txt"
        with open(filename, encoding='utf-8', newline="\n") as file:
            lines = file.readlines()
            card_dict.clear()
            i = 0
            while i < len(lines):
                key = lines[i][:-2]
                key_list.append(lines[i][:-2])
                i += 1
                if i < len(lines):
                    card_dict[key] = lines[i][:-2]
                i += 1
        max_size = len(key_list) - 1
        rand_key = key_list[randint(0, max_size)]
        print(rand_key)
    elif char == 'o':  # done!
        out_list = card_dict.items()
        with open('w'+filename, 'w', encoding='utf-8', newline="\r\n") as file:
            for item in out_list:
                first = item[0] + '\n'
                second = item[1]+'\n'
                file.write(first)
                file.write(second)
    else:
        print(card_dict[rand_key])
        rand_key = key_list[randint(0, max_size)]
        print(rand_key)
print("До свидания!")
