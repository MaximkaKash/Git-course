# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
# Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
# стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).

class Car:
    def __init__(self, firm, model, age, speed):
        self.firm = firm
        self.model = model
        self.speed = speed
        self.age = age

    def vol_speed(self):
        self.speed = self.speed + 5

    def min_speed(self):
        self.speed = self.speed - 5

    def stop(self):
        self.speed = 0

    def speeed(self):
        print(self.speed)

    def n_speed(self):
        self.speed *= -1

    def print_all(self):
        print(self.firm, self.model, self.age, self.speed)


car = Car(firm="Mercedes", model="E500", age=2000, speed=0)

dict = {"1": [car.vol_speed(), car.speeed()],
        "2": [car.min_speed(), car.speeed()],
        "3": [car.n_speed(), car.speeed()],
        "4": [car.print_all(), car.speeed()]}

while car.speed != 100:
    car.vol_speed()
    car.speeed()
car.print_all()

while True:
    choice = input()
    if choice == "0":
        break
    else:
        dict[choice][0]
        dict[choice][1]
