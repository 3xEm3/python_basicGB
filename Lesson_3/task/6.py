"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str):
    word = word.capitalize()
    return word


def user_temp(string: str):
    return ' '.join(map(int_func, string.split(' ')))


user_world = int_func(input("Введите любое слово >>> "))

print(user_world)

user_string = user_temp(input("Введите строку через пробел >>> "))

print(user_string)
# _______________________________
# Введите любое слово >>> стих
# Стих
# Введите строку через пробел >>> ночь улица фонарь аптека
# Ночь Улица Фонарь Аптека
 
