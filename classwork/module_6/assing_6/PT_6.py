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
        print("1")


    elif command == '2':
        print('2')


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
        
        

    elif command == '4':
        print(
            """
            ==================================\n
              You have exited the program
            """)
        break
    else:
        print("Invalid command, please try again")