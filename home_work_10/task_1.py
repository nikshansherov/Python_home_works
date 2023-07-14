# Задача №1 домашнего задания 10.
class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name

    @staticmethod
    def create_animal(name, tail, animal_type):
        if animal_type == 'рыба':
            b = Fish(name, tail)
            print(b.tail)
            return b
        elif animal_type == 'птица':
            return Birds(name, tail)
        elif animal_type == 'млекопитающее':
            return Mammals(name, tail)
        return f'{animal_type} - неизвестный тип животного'


class Fish(Animals):
    def __init__(self, name, tail):
        super().__init__(name, tail)

    def check_deep(self):
        if self.tail <= 3:
            return f'мелководная - обитает на глубине до 3 метров'
        elif self.tail > 3 and self.tail <= 20:
            return f'cреднеглубинная - обитает на глубине от 3 до 20 метров'
        else:
            return f'глубоководная - обитает на глубине более 20 метров'


class Birds(Animals):
    def __init__(self, name, tail):
        super().__init__(name, tail)

    def specific(self):
        wing_len = self.tail * 0.45
        return f'длина крыла - {wing_len} метра'


class Mammals(Animals):
    def __init__(self, name, tail):
        super().__init__(name, tail)

    def specific(self):
        if self.tail < 0.5:
            return f'мелкое животное, высота холки менее 0,5 метра'
        elif self.tail >= 0.5 and self.tail <= 1:
            return f'среднее животное, высота холки в пределах от 0,5 до 1 метра'
        return f'крупное животное, высота холки более 1 метра'


carp = Animals.create_animal('карп', 5, 'рыба')
print(f'название: {carp.name}, {carp.check_deep()}')
eagle = Animals.create_animal('орел', 3, 'птица')
print(f'название: {eagle.name}, {eagle.specific()}')
bear = Animals.create_animal('медведь', 1.5, 'млекопитающее')
print(f'название: {bear.name}, {bear.specific()}')
