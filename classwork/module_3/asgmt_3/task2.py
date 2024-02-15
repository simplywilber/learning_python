# Write a python program to print the largest and smallest of n numbers.

# Create a list 
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create empty largest and smallest number variables
largest_number = nlist[0]
smallest_number = nlist[0]

# Use for loop with embedded if condition statement in order to find largest and lowest numbers
for n in nlist:
    if n > largest_number:
        largest_number = n
    
    if n < smallest_number:
        smallest_number = n
    
# Final output
print(f"The largest number is: {largest_number}")
print(f"The smallest number is: {smallest_number}")

    