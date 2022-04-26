with open('file_test.txt', 'w', encoding='utf-8') as f:
    my_str = None
    while not my_str == '':
        my_str = input('Поочерёдно вводите строки для записи: ')
        f.writelines(my_str + '\n')
        
