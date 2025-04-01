class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # method
    def change_color(self, new_color):
        print(f'Changed color from {self.color} to {new_color}.')
        self.color = new_color


class Plane(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)


class Car(Transport):
    # class attribute
    counter = 0

    # constructor               # parameters
    def __init__(self, model, year, color, penalties=0):
        # fields / attributes
        super().__init__(model, year, color)
        self.penalties = penalties
        Car.counter += 1

        # method

    def drive(self, city):
        if self.penalties > 0:
            print(f'Car {self.model} is driving accurately to {city}.')
        else:
            print(f'Car {self.model} is driving fast to {city}.')


class Truck(Car):
    counter = 0
    def __init__(self, model, year, color, load_capacity, penalties=0):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, type_of_product):
        if self.load_capacity < weight:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded {type_of_product} ({weight} kg) on {self.model}.')


print(f'Factory CAR produced {Car.counter} cars.')
num = 5
bmw_car = Car('BMW X5', 2020, 'red')
print(num)
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'blue'
bmw_car.change_color('blue')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

honda_car = Car('Honda Fit', 2022, 'silver', 900)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

nissan_car = Car(model='Nissan Patrol', penalties=300, color='yellow', year=2000)
print(f'MODEL: {nissan_car.model} YEAR: {nissan_car.year} COLOR: {nissan_car.color} '
      f'PENALTIES: {nissan_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Kant')

boeing_plane = Plane('Boeing 771', 2024, 'white')
boeing_plane.change_color('black')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

mercedes_truck = Truck('Mercedes Actros', 2021, 'orange', 45000)
print(f'MODEL: {mercedes_truck.model} YEAR: {mercedes_truck.year} COLOR: {mercedes_truck.color} '
      f'PENALTIES: {mercedes_truck.penalties} LOAD CAPACITY: {mercedes_truck.load_capacity}')
mercedes_truck.load_cargo(50000, 'Apples')
mercedes_truck.load_cargo(20000, 'Tomatoes')
mercedes_truck.drive('Naryn')

print(f'Factory CAR produced {Car.counter} cars.')
print(f'Factory TRUCK produced {Truck.counter} trucks.')
print('End')
