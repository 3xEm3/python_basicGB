"""
5.Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = float(input("Введите выручку фирмы >>> "))
costs = float(input("Введите издержки фирмы >>> "))
profit = revenue - costs  # прибыль = выручка - издержки

if revenue > costs:
    profitability = profit / revenue
    print(f"Фирма в прибыли. Прибыль равна: {profit:.2f}. Рентабельность равна: {profitability:.2f}")

    employees = int(input("Введите численнсть сотрудников фирмы >>> "))

    profit_employees = profit / employees
    print(f"Прибыль в расчете на одного сотрудника: {profit_employees:.2f}")
else:
    print("Фирма в убытке.")
# ___________________
# Введите выручку фирмы >>> 100.54
# Введите издержки фирмы >>> 56.78
# Фирма в прибыли. Прибыль равна: 43.76. Рентабельность равна: 0.44
# Введите численнсть сотрудников фирмы >>> 10
# Прибыль в расчете на одного сотрудника: 4.38