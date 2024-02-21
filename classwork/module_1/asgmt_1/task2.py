# Task 2
# Write a Python program to compute the following equation. 
# Input the value of x and y and display the value of k,l,m and n. 
# Use mathematical function for power.
# k=x^2 + y^2
# l=x^2 + 2k + y
# m=xy
# n=k^2+l^2+y+m

# Inputs as integers for x and y
x = int(input("Enter first number here:"))
y = int(input("Enter second number here:"))

# Finding the value of k
k = pow(x, 2) + pow(y, 2)

# Finding the value of l
l = pow(x, 2)+ (2 * k) + y

# Finding the value of m
m = x * y

# Finding the vale of n
n = pow(k, 2) + pow(l, 2) + y + m

# Final outputs for k, l, m and n
print(f"The value of k is: {k}")
print(f"The value of l is: {l}")
print(f"The value of m is: {m}")
print(f"The value of n is: {n}")