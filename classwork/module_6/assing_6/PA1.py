# Initial user input
user_input = list(map(int, input("Please enter a list of integers separated by spaces: ").split()))

# Creating a function for finding the smallest and second smallest integers
def finding_small_numbers(numbers):
    
    # Creating two values with positive infinity to be changed in the for loop
    smallest = float('inf')
    sec_smallest = float('inf')
    
    # Checking to see if there are at least two integers to find two small numbers
    if len(user_input) < 2:
        return "Please enter at least two integers"
    else:
        for num in numbers:
            if num < smallest:
                sec_smallest = smallest
                smallest = num
            elif num < sec_smallest:
                sec_smallest = num
        
        # Returning smallest and sec_smallest to display in the output
        return smallest, sec_smallest
    
# Finding the smallest and second smallest by providng the finding_small_numbers function an arguement
smallest, sec_smallest = finding_small_numbers(user_input)

# Printing the final output
print(f"The smallest integer is: {smallest}\nThe second smallest integer is: {sec_smallest}")


    
            

