"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка, т.е. нажат "Энтер" без ввода данных.
"""

with open('1.1.txt', 'a+', encoding='UTF-8') as file:
    while True:
        user_input = input("Напишите что-нибудь >>> ")

        if not user_input:
            break
        file.write(f"{user_input}\n")

# Напишите что-нибудь >>> привет. как дела?
# Напишите что-нибудь >>> хорошего дня!
# Напишите что-нибудь >>>
     
