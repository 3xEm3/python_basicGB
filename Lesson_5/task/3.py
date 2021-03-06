"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
with open("3.1.txt", encoding='utf-8') as f:
    # Читаем его построчно:
    lines = f.readlines()

    salary = []

    for line in lines:
        line = line.split()
        if float(line[1]) < 20000:
            print(f"оклад менее 20 тыс.: {line[0]}")
        salary.append(line[1])
    print(f"средняя величина дохода: {round(sum(map(float, salary)) / len(salary), 2)}")
________________________________________
оклад менее 20 тыс.: Петров
оклад менее 20 тыс.: Сидоров
средняя величина дохода: 21975.43
    
