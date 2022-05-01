"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)



class Equipment:
    def __init__(self, name, count, year):
        self.name = name
        self.count = count
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.count} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, count, year):
        super().__init__(name, count, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.count} {self.year}'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, count, year):
        super().__init__(name, count, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, count, year):
        super().__init__(name, count, year)

    def action(self):
        return 'Копирует'


sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('Canon', 4, 2016)
sklad.add_to(scaner)

scaner = Scaner('hp', 2, 2000)
sklad.add_to(scaner)

printer = Printer('e-320', 'sony', 126, 2018)
sklad.add_to(printer)

xerox = Xerox('hp', '77', 2020)
sklad.add_to(xerox)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Scaner')
print()
print(sklad._dict)

print(scaner.action())
print(printer.action())
print(xerox.action())