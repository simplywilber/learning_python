# Inital user input
nums = input("Enter elements of a list separated by space: ")

# For loops used to extract integers 
str_extraction = [i for i in nums.split() if i.isdigit()]
int_extraction = [int(i) for i in nums.split() if i.isdigit()]

# Create odd numbers list

odd_numbers = []
# Finding odd numbers

for x in int_extraction:
    if x % 2 != 0:
        odd_numbers.append(x)

# Final output
print(f'The string list is: {str_extraction}')
print(f'The user list is: {int_extraction}')
print(f'The odd numbers list is: {odd_numbers}')
