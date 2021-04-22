class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return('Машина поехала')

    def stop(self):
        return('Машина остановилась')

    def turn(self):
        return('Машина повернула')

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышаешь скорость, Ковбой!')
        else:
            print(self.speed)

class SportCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышаешь скорость, Ковбой!')
        else:
            print(self.speed)

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

bmw = TownCar(speed = 80, color ='red', name ='BMW')

bmw.show_speed()
print(bmw.is_police)

audi = WorkCar(speed = 20, color ='blue', name ='Audi', is_police=True)

audi.show_speed()
print(audi.is_police)

dodge = PoliceCar(speed = 100, color ='white', name ='Dodge')

print(dodge.show_speed())
print(dodge.is_police)