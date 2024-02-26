print(
    f"""
    =====================================================
            Choose an activity from the list:
    =====================================================
                [1] - Problem Activity #1
                [2] - Problem Activity #2
                [3] - Problem Activity #3
                [4] - Exit/Quit

    """
)

choice = int(input("              Please enter your choice: "))

print(
    """
    =====================================================
    """)
if choice == 1:
    print(
        """
            Welcome to problem activity #1
        """
          )
    
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



elif choice == 2:
    print(
        """
            Welcome to problem activity #2
        """
          )
    
    # Initial user input
    nums = input("Please enter your numbers here separated by a space: ")

    # Create a new list and mmax variable
    nums_extraction = [int(i) for i in nums.split() if i.isdigit()]
    min = 20
    second_min = 25

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


elif choice == 3:
    print(
        """
            Welcome to problem activity #2
        """
          )
    num = int(input("           Please enter your number here: "))
elif choice == 4 or choice != 1 or choice != 2 or choice != 3:
    print(
        """
               You have exited the list
        """
          )




