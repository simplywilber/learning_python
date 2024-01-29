# Task 2
# Write a Python program to compute the following equation. 
# Input the value of x and y and display the value of k,l,m and n. 
# Use mathematical function for power.
# k=x^2 + y^2
# l=x^2 + 2k + y
# m=xy
# n=k^2+l^2+y+m

x = int(input("Enter first number here:"))
y = int(input("Enter second number here:"))

k = pow(x, 2) + pow(y, 2)
print("k=", k)

l = pow(x, 2)+ (2 * k) + y
print("l=", l)

m = x * y
print("m=", m)

n = pow(k, 2) + pow(l, 2) + y + m
