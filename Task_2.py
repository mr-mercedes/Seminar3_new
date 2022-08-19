# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def read_file():
    data = None
    with open('Fruits.txt', 'r', encoding='utf-8') as file:
        data = file.read().split(', ')

    return data


def find_fruit(first_letter, list_of_fruits):
    new_fruits = []
    for i in range(len(list_of_fruits)):
        if first_letter.lower() == list_of_fruits[i][0].lower():
            new_fruits.append(list_of_fruits[i])

    return new_fruits


first_letter_of_fruit = input('Введите первую букву фрукта: ')
fruits = find_fruit(first_letter_of_fruit, read_file())
print(fruits)
