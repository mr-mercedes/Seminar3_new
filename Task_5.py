# Задача 4. Считайте строковые данные из файла.
# Создайте словарь, содержащий все символы в файле.

def read_file():
    data = None
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split()

    return data


def create_dict(book):
    dict_of_symbols = []
    for item in book:
        for i in range(len(item)):
            if item[i] not in dict_of_symbols:
                dict_of_symbols.append(item[i])

    return dict_of_symbols


some_book = read_file()
symbols = create_dict(some_book)
print(symbols)
