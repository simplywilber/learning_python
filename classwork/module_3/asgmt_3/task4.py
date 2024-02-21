# Write a python program to produce following design:
# Enter a number: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Number input determining rows and columns
num = int(input("Please enter your number here: "))

# For loop to create pyramid
for i in range(1, num +1):
    
    for j in range(i):
        print(i, end=" ")
    # Final output    
    print()

