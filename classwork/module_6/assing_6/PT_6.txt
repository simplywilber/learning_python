import time

# Creating the menu
menu_prompt=(
            """
                   Wilber Amaya-Maurisio\n
            ==================================\n
              Welcome to Programming Task #6\n
            ==================================\n
                1. Problem Activity #1\n
                2. Problem Activity #2\n
                3. Problem Activity #3\n
                4. Exit\n
              Please enter your selection: """)

# Runs the program
while True: # exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
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
        
        # Using time delay for easy readability
        time.sleep(1.2)

    elif command == '2':
            # Initial user input
            user_input = input("Please enter your list of integers separated by spaces: ")
            integers_list = [int(i) for i in user_input.split() if i.strip().isdigit()]

            # Check if the number of inputs exceeds 9
            if len(integers_list) > 9:
                print("Too many inputs, please try again")
            else:
                # Find the middle item
                middle_index = len(integers_list) // 2
                middle_item = integers_list[middle_index]
                print(f"The middle item is: {middle_item}")
                
                # Using time delay for easy readability
                time.sleep(1.2)

    elif command == '3':
        # Creating an initial user input
        user_input = input("Please enter your list of integers: ")

        # Creating a list and using a for loop to split and add only integers
        initial_list = [int(x) for x in user_input.split() if x.isdigit()] 

        # Defiing th e remove_odds() function
        def remove_odds(initial_list):
            #creating a new even list
            new_even_list = []
            
            # Using a for loop to find even numbers using the modulos operator
            for i in initial_list:
                if i % 2 == 0:
                    new_even_list.append(i)

            #Printing new list with only even integers
            print(f"The new list with only even numbers is: {new_even_list}")

        # Calling the remove_odds() function
        remove_odds(initial_list)
        
        # Using time delay for easy readability
        time.sleep(1.2)
        
    elif command == '4':
        print(
            """
            ==================================\n
              You have exited the program
            """)
        break
    else:
        print("Invalid command, please try again")