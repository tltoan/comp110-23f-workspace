"""Instantiating a Class."""

# This is where we instatiate the class, we defined in classes.py ei - we are creating objects that belong to the class

# import the class
# from <file_name>. <module_name> import <classes>
from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("skinny", 10, True)  # Constructor

# access/set/update attribute values
# my_pizza.size = "skinny"
# my_pizza.toppings = 2
# my_pizza.gluten_fre = True
# my_pizza.toppings = 12

print("Size: ")
print(my_pizza.size)  # python -m lessons.classes.pizza_order
print(my_pizza.toppings)

print("Pizza class:")
print(Pizza)

# Make sals_pizza size medium, 5 toppings, Not gluten free
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)


def price(input_pizza: Pizza) -> float:
    """Compute the price of a pizza."""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost


print(price(my_pizza))
print(price(sals_pizza))
print(sals_pizza())

# Add Toppings
my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_topping_new_order(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)