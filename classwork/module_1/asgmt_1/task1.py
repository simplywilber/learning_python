import math

# Task 1
# Create a python program to find the area, circumference and 
# diameter of a circle. Use math function for the value of π and power. 
# Write the proper expression for each formula.

r = int(input("Enter the radius here:"))

area = round(math.pi * pow(r, 2), 4)
print(f"The area is {area}")

circumfrence = (2 * (math.pi)) * r
print(f"The circumfrence is {circumfrence}")

diameter = 2 * r
print(f"The diameter is {diameter}")
