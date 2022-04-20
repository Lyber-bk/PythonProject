with open('text_5.txt', 'w+', encoding='utf-8') as n:
    n.writelines('21 12 54 32')

with open('text_5.txt', 'r', encoding='utf-8') as n:
    num_list = list(map(int, ((n.readlines())[0]).split()))
    print(sum(num_list))
