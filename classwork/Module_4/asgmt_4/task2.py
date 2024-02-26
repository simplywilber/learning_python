# Initial user input
nums = input("Please enter your numbers here separated by a space: ")

# Create a new list and mmax variable
nums_extraction = [int(i) for i in nums.split() if i.isdigit()]
min = nums_extraction[0]
second_min = nums_extraction[1]

# Using for loop to find min and second min for comparison
for x in nums_extraction:
    if x < min:
        min = x

for i in nums_extraction:
    if i > min and i < second_min:
        second_min = i

# Final output
print(f"The user list is: {nums_extraction}")
print(f"The second smallest number is: {second_min}")
