import math


class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
        self.__color = list(color)
        self.filled = True
        self.__sides = self.__validate_sides(sides)

    def __validate_sides(self, sides):
        if len(sides) == self.sides_count:
            return list(sides)
        elif len(sides) == 1 and self.sides_count > 1:
            return [sides[0]] * self.sides_count
        else:
            return [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, (int, float)) and side > 0 for side in sides) and len(sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def get_square(self):
        return None


class Circle(Figure):
    def __init__(self, color, radius):
        self.sides_count = 1
        super().__init__(color, radius)

    @property
    def __radius(self):
        return self.get_sides()[0]

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    def __init__(self, color, side):
        self.sides_count = 12
        super().__init__(color, *([side] * 12))

    def get_volume(self):
        side = self.get_sides()[0]
        return int(side ** 3)


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216