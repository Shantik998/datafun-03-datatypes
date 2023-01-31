"""
Shanti Kandel
Data Analytics project 3
01/29/2023

"""

import random 

# Define a string list
list_brands = ["Nike", "Adidas", "Puma", "Reebok", "Converse", "Vans"]
print
# Define a list of shoe types
list_types = ["sneakers", "boots", "sandals", "flip flops", "loafers", "heels"]

# Define a list of shoes materials
list_materials = ["leather", "canvas", "suede", "nylon", "mesh", "rubber"]

# Define a list for shoes size
list_sizes = ["6", "7", "8", "9", "10", "11"]

# Define a list of colors
list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Define a list of shoes widths
list_widths = ["narrow", "medium", "wide", "extra wide"]

# Define a list of shoe soles
list_soles = ["foam", "gel", "air", "memory foam"]

# Define a list of shoes patterns
list_patterns = ["solid", "striped", "checked", "polka dotted", "floral", "animal print"]


# Define a list of shoe styles
list_styles = ["athletic", "casual", "dressy", "sporty", "outdoor", "fashion"]


divider = "=============================================================="


"""
Using len , set and zip functionx

"""

# Use the len function to get the number of items in each list
num_brands = len(list_brands)
num_types = len(list_types)
print("Number of brands:", num_brands)
print("Number of types:", num_types)

# Use the set function to get a set of unique items from each list
unique_brands = set(list_brands)
unique_types = set(list_types)
print("Unique brands:", unique_brands)
print("Unique types:", unique_types)

# Use the zip function to combine the two lists into a dictionary
brand_mapping = dict(zip(list_brands, list_types))
print("Brand to type mapping:", brand_mapping)


"""
 Using random.choice() to pick a random value from one of the lists.

"""
random_brand = random.choice(list_brands)
print("Random brand:", random_brand)

divider = "=============================================================="

"""
Use open(), read(), split(), and len() to create a list of unique
words from a provided text
"""
