import math


class Figure:
    def __init__(self, color=None, sides=None):
        self.__color = color if color else [0, 0, 0]
        self.__sides = sides if sides else []
        self.filled = False

    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        raise NotImplementedError("Perimeter must be implemented by child classes")

    def set_sides(self, *new_sides):
        if not self.__is_valid_sides(*new_sides):
            return
        self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color=None, radius=None):
        super().__init__(color, [radius])
        self.__radius = radius

    def get_square(self):
        return self.__radius ** 2 * math.pi

    def __len__(self):
        return 2 * self.__radius * math.pi


class Triangle(Figure):
    def __init__(self, color=None, sides=None):
        super().__init__(color, sides)

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    def __init__(self, color=None, side=None):
        super().__init__(color, [side] * 12)
        self.__side = side

    def __len__(self):
        return sum(self.__sides)

    def get_volume(self):
        return self.__side ** 3


# Пример использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)
print(circle1.get_sides())  # [15]

# Проверка периметра (круга)
print(circle1.__len__())  # 62.83185307179586

# Проверка объёма (куба)
print(cube1.get_volume())  # 216