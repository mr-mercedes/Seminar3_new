# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def feb(number):
    if number <= 1:
        return number
    return feb(number - 1) + feb(number - 2)


def create_feb_list(number):
    feb0 = 0
    feb1 = 1
    feb_list = [feb0, feb1]
    for i in range(2, number + 1):
        feb_list.append(feb(i))

    return feb_list


def write_file(list_feb):
    with open('Febonaci_list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{list_feb}\n')


user_input = int(input('Введите количество чисел Фибоначи: '))
feb_list = create_feb_list(user_input)
write_file(feb_list)
