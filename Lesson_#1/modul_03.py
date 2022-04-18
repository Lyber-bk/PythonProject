# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input('Введите число: '))
max_number = 0
while number:
    n_max = number % 10
    if n_max > max_number:
            max_number = n_max
    number = number // 10
print(max_number)
