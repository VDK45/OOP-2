from abc import ABC, abstractmethod


class Cloud(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_square_c(self):
        pass

    @abstractmethod
    def get_square_cos(self):
        pass

    @property
    def get_sq_full(self):
        return str(f'Общая площадь  ткани: {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))}m')


class Coat(Cloud):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на 1 пальто {self.square_c}m'

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_cos(self):
        return self.height * 2 + 0.3


class costume(Cloud):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_cos = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на 1 костюм {self.square_cos}m'

    def get_square_c(self):
        return round(self.width / 6.5 + 0.5)

    def get_square_cos(self):
        return round(self.height * 2 + 0.3)


coat = Coat(3, 5)
costume = costume(4, 6)
print(coat)
print(costume)
print('-------------')
print(coat.get_sq_full)
print('-------------')
print(costume.get_sq_full)
print('-------------')
print(costume.get_square_c())
print(costume.get_square_cos())

print('-' * 15, 'setter для v', '-' * 15)


class MyAbstarctClass(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v <= 0:
            self.__v = abs(v)
        else:
            self.__v = v

    def get_v(self):
        return f"@property Изменение: {str(self.v)}"

    def total(self):
        return f'Общий расход ткани: {self.coat() + self.costume()}'


class coat(MyAbstarctClass):
    def __init__(self, v, h):
        super().__init__(v, h)

    def coat(self):
        return (self.v / 6.5 + 0.5)

    def costume(self):
        return (2 * self.h + 0.3)

    def __str__(self):
        return f'Площадь на 1 пальто {self.coat()}m'


class costume(MyAbstarctClass):
    def __init__(self, v, h):
        super().__init__(v, h)

    def costume(self):
        return (2 * self.h + 0.3)

    def coat(self):
        return (self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на 1 костюм {self.costume()}m'


palto_1 = coat(-700, 5)
print(palto_1)
costume_1 = costume(-6, 8)
print(costume_1)
print(palto_1.total())
print(palto_1.get_v())

print('-' * 15, 'Учительская версия', '-' * 15)


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        return f"{Clothes.result}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)
