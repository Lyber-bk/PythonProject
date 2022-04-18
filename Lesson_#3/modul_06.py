user_str = input('Введите строку из латинских букв:\n')


def correct_symbols(correct=True):
    for i in user_str:
        if i != ' ' and i not in 'abcdefghijklmnopqrstuvwxyz':
            correct = False


    return correct


def result(func, result_str=''):
    if func:
        words = user_str.split()
        for word in words:
            result_str += word.capitalize() + ' '
        return result_str[:-1]
    else:
        return error_msg()


def error_msg():
    return 'Строка должна содержать только латинские буквы в нижнем регистре'

print(result(correct_symbols()))
