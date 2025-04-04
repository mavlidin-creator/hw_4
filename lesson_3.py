class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name


class Car:
    def __init__(self, model, year, color, owner):
        self.__model = model
        self.__year = year
        self.__color = color
        if type(owner) is Person:
            self.__owner = owner

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, Color: {self.__color}, '
                f'Owner: {self.__owner.name}')

    def __lt__(self, other):
        return self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year


class FuelCar(Car):
    __total_fuel = 0

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.show_fuel_amount()

    @classmethod
    def show_fuel_amount(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel} litters of fuel.')

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    def __init__(self, model, year, color, owner, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color, owner)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.')

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, owner, battery):
        Car.__init__(self, model, year, color, owner)
        self.__battery = battery

    def drive(self):
        print(f'Car {self.model} is driving by electricity.')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, owner, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, owner, fuel_bank)
        ElectricCar.__init__(self, model, year, color, owner, battery)

    def drive(self):
        print(f'Car {self.model} is driving by fuel or electricity.')


# some_car = Car('Toyota Camry', 2020, 'red')
# print(some_car)

# FuelCar.total_fuel += 1000
FuelCar.buy_fuel(1000)

person = Person('Jim', 26)
toyota_car = FuelCar('Toyota Camry', 2020, 'red',
                     person, 80)
print(toyota_car)

byd_car = ElectricCar('BYD 350', 2021, 'blue',
                      person, 15000)
print(byd_car)

# person_2 = Person('Jane', 37)
# a        = b
chevrolet_car = HybridCar('Chevrolet Volt', 2023, 'white',
                          Person('Jane', 37), 70, 10000)
print(chevrolet_car)
chevrolet_car.drive()
print(HybridCar.mro())

number_1, number_2 = 3, 8
print(f'Number one is greater than number two: {number_1 > number_2}')
print(f'Number one is less than number two: {number_1 < number_2}')
print(f'Toyota car is cheaper than Chevrolet car: {toyota_car < chevrolet_car}')
print(f'Toyota car is more expensive than Chevrolet car: {toyota_car > chevrolet_car}')
print(f'Toyota car is the same with Chevrolet car: {toyota_car == chevrolet_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Sum of fuel banks: {chevrolet_car + toyota_car}')

# FuelCar.total_fuel -= 100
# print(f'Factory FUEL_CAR has {FuelCar.total_fuel} litters of fuel.')
FuelCar.show_fuel_amount()

print(f'Factory FUEL_CAR uses {FuelCar.get_fuel_type()} fuel type.')
