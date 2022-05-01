"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

class Matrix(object):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return '\n'.join('\t'.join(map(str,row)) for row in self.value)
    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Матрицы разного размера")
            exit(1)



m2x3 = Matrix([[31, 32], [37, 43], [51, 86]])
print(m2x3 + m2x3)
m3x3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m3x3 + m3x3 + m3x3)
m2x4 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(m2x4)



print()