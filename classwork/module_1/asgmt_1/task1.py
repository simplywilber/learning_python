# Task 1
# Create a python program to find the area, circumference and 
# diameter of a circle. Use math function for the value of π and power. 
# Write the proper expression for each formula.

import math

# Input for the radius of a circle
r = int(input("Enter the radius here:"))

# Finding the area of the circle
area = round(math.pi * pow(r, 2), 4)

# Finding the circumfrence of the cricle
circumfrence = (2 * (math.pi)) * r

# Finding the diameter of the circle
diameter = 2 * r

# Final output statements
print(f"The area is {area}")
print(f"The circumfrence is {circumfrence}")
print(f"The diameter is {diameter}")
