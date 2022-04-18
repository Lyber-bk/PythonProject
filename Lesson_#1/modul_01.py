# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

while True:
    use_seconds = int(input('Привет, эта программма переводит секунды \n в часы минуты и секунды \n Введите число '))
    hours = int(use_seconds // 3600)
    minuts = int(use_seconds % 3600) // 60
    seconds = use_seconds % 60
    print(f' {hours:02d} : {minuts:02d} : {seconds:02d} ')
    use_answer = input('Попробуем еще: "да" или "нет" ? ')
    if use_answer == "да":
        continue
    else:
        print("Пока!")
        break

