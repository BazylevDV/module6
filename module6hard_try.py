import math


class Figure:
    """
    Базовый класс для всех геометрических фигур.
    Содержит общие атрибуты и методы для работы с цветом и сторонами фигур.
    """
    def __init__(self, color=(0, 0, 0), sides=[]):
        self._color = color
        self._sides = sides
        self.filled = False

    def get_color(self):
        """Возвращает текущий цвет фигуры."""
        return self._color

    @staticmethod
    def _is_valid_color(r, g, b):
        """Проверяет, является ли цвет допустимым (каждый компонент в диапазоне от 0 до 255)."""
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        """Устанавливает новый цвет фигуры, если он допустим."""
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        """Проверяет, являются ли новые стороны допустимыми."""
        if new_sides:
            return len(new_sides) == len(self._sides) and all(
                isinstance(side, int) and side > 0 for side in new_sides)
        return False

    def get_sides(self):
        """Возвращает текущие стороны фигуры."""
        return self._sides

    def get_perimeter(self):
        """Возвращает периметр фигуры. Должен быть переопределен в дочерних классах."""
        raise NotImplementedError("Perimeter must be implemented by child classes")

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны фигуры, если они допустимы."""
        if not self._is_valid_sides(*new_sides):
            return
        self._sides = list(new_sides)


class Circle(Figure):
    """
    Класс для круга. Наследует от Figure и добавляет специфичные для круга методы.
    """
    def __init__(self, color=(0, 0, 0), radius=None):
        super().__init__(color, [radius])
        self._radius = radius

    def get_square(self):
        """Возвращает площадь круга."""
        return self._radius ** 2 * math.pi

    def get_perimeter(self):
        """Возвращает округленный периметр круга (длина окружности)."""
        return round(2 * self._radius * math.pi)

    def set_sides(self, *new_sides):
        """Устанавливает радиус круга, если передано одно значение."""
        if len(new_sides) == 1:
            self._radius = new_sides[0]
            self._sides = [self._radius]


class Triangle(Figure):
    """
    Класс для треугольника. Наследует от Figure и добавляет специфичные для треугольника методы.
    """
    def __init__(self, color=(0, 0, 0), sides=[]):
        super().__init__(color, sides)

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона."""
        a, b, c = self._sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def get_perimeter(self):
        """Возвращает периметр треугольника."""
        return sum(self._sides)


class Cube(Figure):
    """
    Класс для куба. Наследует от Figure и добавляет специфичные для куба методы.
    """
    def __init__(self, color=(0, 0, 0), side=None):
        super().__init__(color, [side] * 12)
        self._side = side

    def get_perimeter(self):
        """Возвращает периметр куба (сумма длин всех ребер)."""
        return sum(self._sides)

    def get_volume(self):
        """Возвращает объем куба."""
        return self._side ** 3


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
print(circle1.get_perimeter())  # 94

# Проверка объёма (куба)
print(cube1.get_volume())  # 216