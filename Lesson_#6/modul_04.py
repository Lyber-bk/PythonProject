class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nCкорость {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость {self.speed} км/ч  *Нарушение скоростного режима*!!!'
        else:
            return f'Скорость {self.name} не превышена'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышение скорости!!! Скорость {self.speed} км/ч'
        else:
            return f'Скорость {self.name} не превышена'


class PoliceCar(Car):
    pass


town = TownCar('Lada Largus', 70, 'белая', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Porsh', 170, 'черный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Газель', 30, 'белая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Полицейская Skoda', 100, 'серая', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())
