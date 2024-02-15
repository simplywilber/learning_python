# Write a python program to produce following design:
# Enter a number: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Number input determining rows and columns
num = int(input("Please enter your number here: "))

# For loop to determine the rows
for x in range(0, num):

    # Inner for loop to determine the columns
    for y in range(x+1):
        num= 1
        num+=1
        
        # The end will provide space needed for the pyrami
        print(num , end=" ")
    print("\n") 
    num+=1

