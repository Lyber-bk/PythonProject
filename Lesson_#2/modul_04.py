# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово
# с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые
# 10 букв в слове.

my_string = input('Введите строку из нескольких слов через пробел: ').split()
for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')
