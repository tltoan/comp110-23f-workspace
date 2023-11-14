"""CQ07 Intro to OOP."""


from __future__ import annotations


class Point:
    """This represents my class."""

    x: float
    y: float

    def __init__(self, x_input=0.0, y_input=0.0):
        """Constructor."""
        self.x = x_input
        self.y = y_input
    
    def scale_by(self, factor: int) -> None:
        """Scale method."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """New Point method."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def __str__(self) -> str:
        """Printing out the points."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplier."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def __add__(self, add_by: int | float) -> Point:
        """Add function."""
        new_x = self.x + add_by
        new_y = self.y + add_by
        new_point: Point = Point(new_x, new_y)
        return new_point
