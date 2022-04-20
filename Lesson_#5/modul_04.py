from googletrans import Translator

tr = Translator(to_lang='ru')
with open('Lesson_#5\\text_4.txt', 'r', encoding='utf-8') as f_obj:
    ftext = [str.strip().split() for str in f_obj]
for el in ftext:
    el.insert(0, tr.translate((el.pop(0))))
ftext = [' '.join(el) for el in ftext]
with open('text_4_1.txt', 'w', encoding='utf-8') as f_obj2:
    for el in ftext:
        f_obj2.writelines(f'{el}\n')
