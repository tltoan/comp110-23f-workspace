"""Defining a Class!"""

# This of a class definition as a "roadmap" for objects that belong to the class, you are defining the underlying structure every instance of this class will have

from __future__ import annotations


class Pizza:
    """This is my class to represent pizza!"""

# attributes
# syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constructor."""
        self.size = size_input
        self.toppings = toppings_input
        self.gf_input = gf_input

    def price(self) -> float: 
        """Method to compute price of pizza."""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int):
        """Update an existing pizza order with num_toppings."""
        self.toppings += num_toppings

    def add_topping_new_order(self, num_toppings: int) -> Pizza:
        """Make new pizza using existing info."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza