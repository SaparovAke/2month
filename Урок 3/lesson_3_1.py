from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


class MusicPlayable:
    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print('Music stopped')


class Drawable:
    def draw(self, emoji):
        print(emoji)


class Smartphone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError('Color attruibute must be of data type Color')

    @property
    def color(self):
        return self.__color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print('I can drive')

    def __str__(self):
        return f'Model: {self.model} year: {self.year} color: {self.__color}'

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __neg__(self):
        return self.year != other.year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @staticmethod
    def get_fuel_type():
        return 'AI 98'

    def __init__(self, model, year, fuel_bank, color):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print('I can drive by using fuel')

    def __str__(self):
        return super().__str__() + f' fuel bank: {self.fuel_bank}'

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, battery, color):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    def drive(self):
        print('I can drive by using electricity')

    def __str__(self):
        return super().__str__() + f' battery: {self.battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, fuel_bank, battery, color):
        ElectricCar.__init__(self, model, year, battery, color)
        FuelCar.__init__(self, model, year, fuel_bank, color)


nissan_car = FuelCar('Nissan Skyline', 2020, 30, Color.RED)
print(nissan_car)

tesla_car = ElectricCar('Tesla Model X', 2022, 80000, Color.GREEN)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2019, 45, 20000, Color.YELLOW)
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())
toyota_car.play_music('Beliver')
toyota_car.draw('🚗')

smartphone = Smartphone()
smartphone.play_music('Promise')
smartphone.draw('📱')

if tesla_car.model == 'Tesla ModelX':
    print('Tesla is very good!')

if tesla_car.color == Color.GREEN:
    print('The car is beautiful')

number_1 = 9
number_2 = 5

print(f'Number 1 is bigger than Number 2 {number_1 > number_2}')
print(f'Nissan is bigger than Prius {nissan_car > toyota_car}')

print(f'Total fuel amount: {nissan_car + toyota_car}')

print(FuelCar.get_total_fuel_amount())
# FuelCar.__total_fuel_amount -= 100
print(FuelCar.get_total_fuel_amount())
print(f'Fuel type: {FuelCar.get_fuel_type()}')
