"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Add two points together."""
        return Point(self.x + rhs.x, self.y + rhs.y)

    def scale(self, factor: float) -> Point:
        """Immutable: multiplies components by factor without mutation."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)

        return scaled_point

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"(Point({self.x}, {self.y})"

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
p2: Point = p0 * 2.0
p3: Point = p0 + p2
print(f"p0{p0}")
print(f"p1{p1}")
print(f"p2{p2}")
print(f"p3{p3}")

print(p0[0])
print(p0[1])

p1_repr: str = repr(p1)
print(p1_repr)
