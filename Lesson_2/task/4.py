"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("Введите несколько слов через пробел >>> ").split(" ")

for ind, el in enumerate(user_input):
    print(f"{ind+1} >>> {el[:10]}")
# ____________________________________________
# Введите несколько слов через пробел >>> hello world !!! 112233445566778899 hi
# 1 >>> hello
# 2 >>> world
# 3 >>> !!!
# 4 >>> 1122334455
# 5 >>> hi
 