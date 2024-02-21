# Write a python program to print sum of odd and even numbers up to n

# Created a list
nlist = [1, 2, 3, 4, 5, 6, 7 ,8, 9 , 10]

# Created empty variables
even_numbers_sum = 0
odd_numbers_sum = 0

# Created empty even and odd number lists
even_numbers = []
odd_numbers = []

# Using modulo to find even numbers, else is odd
for n in nlist:
    if n % 2 == 0:
        even_numbers.append(n)
        even_numbers_sum += n
    else:
        odd_numbers.append(n)
        odd_numbers_sum += n

# Final output
print("All even numbers are:", *even_numbers)
print("All odd numbers are:", *odd_numbers)
print(f"The sum of even numbers is: {even_numbers_sum}")
print(f"The sum of odd numbers is: {odd_numbers_sum}")