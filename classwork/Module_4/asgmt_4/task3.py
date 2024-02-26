# Initial user input
nums = input("Please enter your numbers here separated by a space: ")

# Create a new list and mmax variable
nums_extraction = [int(i) for i in nums.split() if i.isdigit()]
max = 0
second_max = 0

# Using for loop to compare max and second max
for x in nums_extraction:
    if x > max:
        max = x

for i in nums_extraction:
    if i < max and i > second_max:
        second_max = i
        
# Final output
print(f"The user list is: {nums_extraction}")
print(f"The second largest number is: {second_max}")
