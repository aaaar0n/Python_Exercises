# #Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math

r = float(input("Input radius value: "))
area = math.pi * r**2
print(area)