# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.


def bot(user_phrase):
    bot_answer = \
        {
            "Команды": "'Привет', 'Как тебя зовут','Что ты умеешь', 'Выход'",
            "Привет": "Привет, Как тебя зовут?",
            "Как тебя зовут": "Меня зовут бот-Сережка, а тебя как зовут?",
            "Что ты умеешь": "Я умею всякое, тебе лучше не знать",
            find_name(user_phrase): f"Привет {user_phrase}, приятно познакомиться",
            "Выход": "Пока пока",
        }

    return bot_answer.get(user_phrase)


def find_name(name):
    names = None
    with open('names.txt', 'r', encoding='utf-8') as file:
        names = file.read().split(', ')

    for i in range(len(names)):
        if name.lower() == names[i].lower():
            return names[i]


user_input = input('Система СКАЙНЕТ активированна: ')
while True:
    if user_input == "Выход":
        main = bot(user_input)
        print(main)
        break
    elif user_input == "Команды":
        main = bot(user_input)
        print(f"Список команд бота --> {main}")
    elif user_input == find_name(user_input):
        main = bot(user_input)
        print(main)
    elif bot(user_input) is None:
        print(f"Неизвестная команда {user_input}, для помощи введите 'Команды'")
    else:
        main = bot(user_input)
        print(main)
    user_input = input('Бот ждет команды: ')
