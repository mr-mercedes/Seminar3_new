# Задача 3. Напишите скрипт генератора паролей
# заданной длины, состоящих из букв и чисел.
# Создайте скрипт для сохранения пароля в файл
# password.txt.

import random
import time


def password_generate(length):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
               'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '&', '?']
    password = ''
    for i in range(length):
        generator = random.randint(1, 4)
        match generator:
            case 1:
                generator = random.randint(0, len(numbers) - 1)
                password += str(numbers[generator])
            case 2:
                generator = random.randint(0, len(letters) - 1)
                password += letters[generator]
            case 3:
                generator = random.randint(0, len(letters) - 1)
                password += letters[generator].lower()
            case 4:
                generator = random.randint(0, len(symbols) - 1)
                password += symbols[generator]
    return password


def write_password(pas):
    seconds = time.time()
    now = time.ctime(seconds)
    with open("pass.txt", 'a', encoding='utf-8') as file:
        file.write(f'Пароль -->[{pas}]<-- создан {now}\n')


password_length = int(input("Введите длину пароля: "))
password = password_generate(password_length)
write_password(password)
