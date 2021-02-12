class Math:
    def __init__(self, x):
        self.x = x

    def __add__(self, other: int):
        print('__add__ use: ')
        return Math(self.x + other.x)

    def __sub__(self, other: int):
        print('__sub__ use: ')
        if self.x >= other.x:
            return Math(self.x - other.x)
        else:
            print(f'{other.x} Biget {self.x} ')
            return Math(other.x - self.x)

    def __mul__(self, other: int):
        print('__mul__ metod')
        return Math(self.x * other.x)

    def __truediv__(self, other: int):
        print('__true__ func')
        if other.x <= 0:
            print('Kletki ne mojet byt <= 0')
        else:
            return Math(round(self.x / other.x))

    def make_order(self, count: int):
        body, row = self.x // count, self.x % count

        print(f'\n{body} ryadov, {row} ostalos\n')
        return '\n'.join(['*' * count] * body + (['*' * row]))

    def __str__(self):
        return f' {self.x}  '


a = Math(7)
print(a)
b = Math(6)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print((a * b).make_order(5))
