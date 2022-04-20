import re

subjects = {}

with open('text_6.txt', 'r', encoding='utf-8') as s:
    for l in s:
        subject = (((l).strip('\n')).split(':'))
        number = re.findall('[0-9]+', subject[1])
        num_sum = sum(list(map(int, number)))
        subjects[(subject[0])] = num_sum
print(subjects)
