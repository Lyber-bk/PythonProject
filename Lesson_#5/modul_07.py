import json

firms = {}
av_prof = {}
sum_prof = 0
prof_firms = 0
with open('text_7.txt', 'r', encoding='utf-8') as s:
    for l in s:
        firm = (((l).strip('\n')).split())
        profit = int(firm[-2]) - int(firm[-1])
        firms[firm[0]] = profit

for val in firms.values():
    if val > 0:
        sum_prof += val
        prof_firms += 1

average_profit = sum_prof / prof_firms
av_prof['average_profit'] = average_profit
final_list = [firms, av_prof]
print(final_list)

with open('text_7.1.json','w', encoding='utf-8') as f:
    json.dump(final_list, f, ensure_ascii=False, indent=4)
    
