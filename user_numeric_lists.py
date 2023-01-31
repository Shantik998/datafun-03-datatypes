"""
Shanti Kandel
Data Analysis project 3 
01/29/2023

The goal of this project is to practice numeric list from the domain.

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats

""" 
list1 is a list of size of shoes from toddler to adult during 1 month.
"""

list_1 = [1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11]

""" 
list_x represents different design
"""
list_x = [3,4,5,6,7,8,9,10,11,12]
"""
list_y represents age of customers who brought shoes

"""

list_y = [5,10,15,20,25,30,35,40,45,50]

print ("list1")

""" 
calculate mean, median, mode, standard deviation, and variance for list_1

"""
print()
mean = stats.mean(list_1)
median = stats.median(list_1)
mode = stats.mode(list_1)
st_dev = stats.stdev(list_1)
variance = stats.variance(list_1)

print(f"shoes size mean: {round(mean,2)}")
print(f"shoes size median:{round(median, 2)}")
print(f"shoes size mode : {round(mode, 2)}")
print(f"shoes size standard deviation:{round(st_dev,2)}")
print(f"shoes size variance:{round(variance, 2)}")

print()

""" 
Calculation for statisttics module to get correlation between list_x and list_y
"""

print()
correlationxy = stats.correlation(list_x, list_y)
slope, intercept = stats.linear_regression(list_x, list_y)
xfuture = 13
yfuture = slope * xfuture + intercept

print(f"Correlation between list_x and list_y :{round(correlationxy, 2)}")
print(f"slope of best-fit line for list_x and list_y: {round(slope, 2)}")
print(f"Intercept of best-fit line for list_x and list_y: {round(intercept, 2)}")
print(f"Predicted age at design 13: {round(yfuture, 2)}")

print()



"""
    Calculating the min and max scores
    
    """

count_min = min(list_1)
count_max = max(list_1)
count_length = len(list_1)
count_sum = sum(list_1)
count_avg = count_sum / count_length
count_set = set(list_1)
count_sorted_for = sorted(list_1)
count_sorted_back = sorted(list_1, reverse=True)

print(f"Minimum shoes size: {count_min}")
print(f"Maximum shoes size: {count_max}")
print(f"Number of counting days: {count_length}")
print(f"Total Number of shoes sizes: {count_sum}")
print(f"Average Number of shoes size: {round(count_avg, 2)}")
print(f" shoes size set: {count_set}")
print(f"shoes size set (Ascending): {count_sorted_for}")
print(f"shoes Sorted (Descending): {count_sorted_back}")

print()


"""
   Calculations of List methods 
    """

list_a = [10, 20, 30, 40, 50, 60, 70]

# adding an element to the end of the list
list_a.append(80)
print(list_a) # [10, 20, 30, 40, 50, 60, 70, 80]

# inserting an element at a specific index
list_a.insert(3, 35)
print(list_a) # [10, 20, 30, 35, 40, 50, 60, 70, 80]

# removing an element by value
list_a.remove(50)
print(list_a) # [10, 20, 30, 35, 60, 70, 80]

# removing an element by index
del list_a[4]
print(list_a) # [10, 20, 30, 35, 70, 80]

# updating a value at a specific index
list_a[2] = 33
print(list_a) # [10, 20, 33, 35, 70, 80]

# sorting the list in ascending order
list_a.sort()
print(list_a) # [10, 20, 33, 35, 70, 80]

# sorting the list in descending order
list_a.sort(reverse=True)
print(list_a) # [80, 70, 35, 33, 20, 10]


"""
Remove the item at index 3 from the new list
fourth = new_scores.pop(3)
print(new_scores)
print(fourth)
print(new_scores)
"""
    
new_scores = [10, 20, 30, 40, 50, 60, 70]
new_size = [10, 11, 12, 13, 14, 15]

# Removing the fourth element of the list
fourth = new_scores.pop(3)

# Printing the list after removing the fourth element
print("new_scores:", new_scores) # new_scores: [10, 20, 30, 50, 60, 70]

# Printing the removed element
print("fourth element:", fourth) # fourth element: 40

# Printing the list again
print("new_scores:", new_scores) # new_scores: [10, 20, 30, 50, 60, 70]

print()

""" 
    Using a filter and map function list
"""


even_squared_numbers = [i**2 for i in new_scores if i % 2 == 0]
list_cubes = [i**3 for i in new_scores]
list_vol = [i**3 for i in new_scores]

print(f"The even age from the list are: {even_squared_numbers}")
print()
print(f"The cube of each temperature in the list are: {list_cubes}")
print()
print(f"The volumes of cubes with sides equal to the values in list1 are {list_vol}")
print()


""" 
    Using list comprehension
"""

# selecting shoes size greater than 13
size_over_13 = [i for i in new_size if i > 13]

# Cast the result using square brackets to get a list
doubled_size = [i*2 for i in new_size]

# Map each element to its square root
sqrt_size = [math.sqrt(i) for i in new_size]

# Map each element (radius) to its area
radius_list = [1, 2, 3, 4, 5]
# Say "map r to pi r squared" and cast to a list
area_list = [math.pi * i**2 for i in radius_list]

print(f"the value bigger than size 13 are{size_over_13}")
print(f" the value of double size are{doubled_size}")
print(f"the value of square root of size{sqrt_size}")
print(f"the area list{area_list}")
print()



