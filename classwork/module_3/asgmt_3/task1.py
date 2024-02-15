# Write a python program to print sum of odd and even numbers up to n

# Create a list
nlist = [1, 2, 3, 4, 5, 6, 7 ,8, 9 , 10]

# Create empty variables
even_numbers_sum = 0
odd_numbers_sum = 0

# Using modulo to find even numbers, else is odd
for n in nlist:
    if n % 2 == 0:
        even_numbers_sum += n
    else:
        odd_numbers_sum += n

# Final output
print(f"The sum of even numbers is: {even_numbers_sum}")
print(f"The sum of odd numbers is: {odd_numbers_sum}")