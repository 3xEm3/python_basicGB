"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys


def salary():
    file, time, money, bonus = sys.argv
    return int(time) * int(money) + int(bonus)


print(f"заработная плата сотрудника >>> {salary()}")
# ___________________
# (venv) vvo@Mac-mini-Vitaly task % python3 ./1.py 40 350 7500
# заработная плата сотрудника >>> 21500

    
