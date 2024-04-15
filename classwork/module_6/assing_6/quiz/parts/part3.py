# Creating a function that handles list
def sum_of_product(list_1, list_2):
    
    # Matching the lengths to verify the size of the lists are the same
    if len(list_1) != len(list_2):
        return "Error: Lists must have the same size."
    
    # Using a for loop in order to find the sum
    result = 0
    for i in range(len(list_1)):
        result += list_1[i] * list_2[i]
    return result

# Sample Input
list1_input = input("Please enter the integers of the List 1: ")
list2_input = input("Please enter the integers of the List 2: ")

# Extracting the integers from the user input
list_1 = [int(i) for i in list1_input.split() if i.strip().isdigit()]
list_2 = [int(i) for i in list2_input.split() if i.strip().isdigit()]

# Output
output = sum_of_product(list_1, list_2)
print("The sum of product is: ", output)