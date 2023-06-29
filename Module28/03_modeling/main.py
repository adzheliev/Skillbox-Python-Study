import math


class Square:
    def __init__(self, side: (int, float)) -> None:
        self.side = side

    @property
    def side(self) -> (int, float):
        return self.side

    @side.setter
    def side(self, side: (int, float)) -> None:
        self.side = side

    def perimeter(self) -> (int, float):
        return self.side * 4

    def area(self) -> (int, float):
        area = self.side ** 2
        return area


class Triangle:
    def __init__(self, base: (int, float), height: (int, float)) -> None:
        self.base = base
        self.height = height

    @property
    def base(self) -> (int, float):
        return self.base

    @base.setter
    def base(self, base:(int, float)) -> None:
        self.base = base

    @property
    def height(self) -> (int, float):
        return self.height

    @height.setter
    def height(self, height: (int, float)) -> None:
        self.height = height

    def perimeter(self) -> (int, float):
        perimeter = self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        return perimeter

    def area(self) -> (int, float):
        area = (self.base * self.height) / 2
        return area

class FigureMixin(Square, Triangle):

    def surface_area(self) -> float:
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area

class Cube(Square, FigureMixin):

    def __init__(self, length: float) -> None:
        super().__init__(length)
        self.surfaces: List[Square] = [Square, Square, Square, Square, Square, Square]

class Piramid(Triangle, FigureMixin):

    def __init__(self, length: float) -> None:
        super().__init__(length)
        self.surfaces: List[Triangle] = [Triangle, Triangle, Triangle, Triangle, Square]
