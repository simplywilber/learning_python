# Importing time for message delay and readbility
import time

# Defining the entire program 
def program_project_4():
    
    # Boolean statement that handles program runtime
    running = True
    
    # While loop that runs program only when running is true
    while running:
        # Main menu
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

        # Initial Input
        choice = (input("                       Please enter your choice: "))

        print(
            """
            =====================================================
            """)
        
        # If statement handling user input
        if choice.isdigit():
            
            # Problem Activity 1  
            if int(choice) == 1:
                print(
                    """
                      Welcome to problem activity #1
                    """
                    )
                
                # Inital user input
                nums = input("Enter elements of a list separated by spaces: ")

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
                
                # Redirect to home menu with a delay for readability
                time.sleep(0.9)
                program_project_4()

            # Problem Activity 2
            elif int(choice) == 2:
                print(
                    """
                      Welcome to problem activity #2
                    """
                    )
                
                # Initial user input
                nums = input("Please enter your numbers here separated by commas: ")

                # Create a new list and max variable
                nums_extraction = [int(i) for i in nums.split(",") if i.isdigit()]
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
                
                # Redirect to home menu with a delay for readability
                time.sleep(0.9)
                program_project_4()

            # Problem Activity 3
            elif int(choice) == 3:
                print(
                    """
                      Welcome to problem activity #3
                    """
                    )
                # Initial user input
                nums = input("Please enter your numbers here separated by commas: ")

                # Create a new list and max variable
                nums_extraction = [int(i) for i in nums.split(",") if i.isdigit()]
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

                # Redirect to home menu with a delay for readability
                time.sleep(0.9)
                program_project_4()

            # Program exit
            elif int(choice) == 4:
                print(
                    """
                        You have exited the program\n
            =====================================================
                    """
                    )
                
                running = False
                break
                
                
            
            # Input error catch if the user selection is invalid
            elif int(choice) < 1 or int(choice) > 4:
                print(
                    """
                        Invalid selection
            Please enter a valid selection from the main menu
                    """
                    )

                # Redirect to home menu with a delay for readability
                time.sleep(1.2)
                program_project_4()
        
        # Input error catch if the user selection is a string  
        else:
            print(
                """
                        Invalid selection
            Please enter a valid selection from the main menu
                """
                )
            
            # Redirect to home menu with a delay for readability
            time.sleep(1.2)
            program_project_4()

# Program execution
program_project_4()