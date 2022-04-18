# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
# сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    enum = num1, num2, num3
    for i in enum:
        if i != min(enum):
            print(i)

my_func(50, 25, 30)
