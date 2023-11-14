"""Practice with dictionary syntax."""


ice_cream: dict[str, int] = {"chocolate": 10, "vanilla": 15, "strawberry": 8, }
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(len(ice_cream))
print("chocolate" in ice_cream)
print("mint" in ice_cream)
print(ice_cream)

# using "in" in a condiitonal
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no mint in icecream.")

# loop through dictionary
for key in ice_cream:
    print(f"there are {ice_cream[key]} orders of {key}")
    