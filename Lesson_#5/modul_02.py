with open('news.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, f'В строке: {len(line.split())} слов', end='')
        print()