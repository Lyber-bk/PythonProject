dict = {}
sum = 0

with open('text_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key = (line.split())[0]
        val = float((line.split())[1])
        dict[key] = val

print('Меньше 20-ти тысяч получают:')
for key, value in dict.items():
    if value < 20000:
        print(key)
    sum += value

print(f'Средняя зарплата : {round(sum / len(dict), 2)} руб.')
