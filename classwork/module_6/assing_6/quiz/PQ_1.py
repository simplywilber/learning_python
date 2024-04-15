import time

# Creating the menu
menu_prompt=(
            """
                   Wilber Amaya-Maurisio\n
            ==================================\n
        Welcome to the Python Programming Final Quiz\n
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
        
        # User input for the phone number
        phone_number = input("Please enter a 10-digit phone number: ")
        
        # Creating a function the splits the phone number
        def format_phone_number(phone_number):
            area_code = phone_number[:3]
            prefix = phone_number[3:6]
            line_number = phone_number[6:]
            formatted_number = f"({area_code}) {prefix}-{line_number}"
            return formatted_number

        # Output
        print(f"The formatted number is: {format_phone_number(phone_number)}")
        
        # Using time module to cause delay for easy reading
        time.sleep(1.2)


    elif command == '2':
        
        # User input for the word sample
        input_words = input("Please enter your sample phrase: ")
        
        # Creating a function to lower and split words
        def word_frequency(words):
            
            # creating a dictionary for frequency
            frequency = {}
            
            # Lowercasing and splitting words
            words = words.lower().split()
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1
            return frequency
        # Creating a function that displays word and frequency
        def print_word_frequency(frequency):
            for word, freq in frequency.items():
                print(word, freq)

        # Getting word frequency by calling the word frequency function
        frequency = word_frequency(input_words)

        # Output
        print_word_frequency(frequency)
        
        # Using time module to cause delay for easy reading
        time.sleep(1.2)

    elif command == '3':
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
        
        # Using time module to cause delay for easy reading
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