# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
arg1 = input('Делимое: ')
arg2 = input('Делитель: ')

def div(*args):
    try:
        return float(arg1) / float(arg2)
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'Не число'


print(div())
