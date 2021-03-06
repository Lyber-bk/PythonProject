class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} пишет'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} чертит'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} рисует'


pen = Pen('ручка')
print(pen.draw())
pencil = Pencil('карандаш')
print(pencil.draw())
handle = Handle('маркер')
print(handle.draw())
