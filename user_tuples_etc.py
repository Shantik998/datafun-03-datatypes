"""
Shanti Kandel
Data Analysis project 3 
01/29/2023

This file is to practice on tuples.
"""
divider = "=============================================================="

import math 

# Create some tuples
height_tuple = (1, 2, 3, 4, 5)
weight_tuple = (100, 200, 300, 400, 500)

# tuple concatenation
tupleCat = height_tuple + weight_tuple

# tuple repetition
tupleAThrice = height_tuple * 3

print(f"{height_tuple = }")
print(f"{weight_tuple = }")
print(f"{tupleCat = }")
print(f"{tupleAThrice = }")

# tuple membership testing

print(3 in height_tuple)
print(150 in weight_tuple)

# Use tuples to return multiple values from a function

def get_height_and_weight():
    height_tuple = (1, 2, 3, 4, 5)
    weight_tuple = (100, 200, 300, 400, 500)
    return height_tuple, weight_tuple

result = get_height_and_weight()
print(result)

# Slice tuples

print(height_tuple[1:4])
print(weight_tuple[:3])

# Tuple repetition

print(height_tuple * 3)
print(weight_tuple * 2)

# tuple indexing

print(height_tuple[2])
print(weight_tuple[-3])

# Concatenate tuples

result = height_tuple + weight_tuple
print(result)

"""
Practice on a set 

"""

sports_cars = {"Ferrari", "Lamborghini", "Porsche", "McLaren"}
suvs = {"Range Rover", "Jeep Grand Cherokee", "Toyota Land Cruiser", "BMW X5"}
print(f"Set 1: {sports_cars}")
print(f"Set 2: {suvs}")

# set union
setC = sports_cars | suvs

# set intersection
setD = sports_cars & suvs

# set difference
setE = sports_cars - suvs

# Add an element
sports_cars.add("Aston Martin")

# Remove an element
sports_cars.remove("Porsche")

# Check the length of the set
print(len(sports_cars))

# Check if an element is in the set
print("Lamborghini" in sports_cars)

# Clear the set
sports_cars.clear()

# Check if the set is empty
print(len(sports_cars) == 0)

