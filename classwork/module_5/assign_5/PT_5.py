import time

# Defining the entire program
def program_project_5():
    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display the main menu
        print(
            """
            =====================================================
                      Choose an activity from the list:
            =====================================================
                         [1] - Problem Activity #1
                         [2] - Problem Activity #2
                         [3] - Problem Activity #3
                         [4] - Exit/Quit

            """
        )

        # Get the user choice
        choice = (input("                       Please enter your choice: "))

        print(
            """
            =====================================================
            """
        )

        # Check if the input is a number
        if choice.isdigit():
            choice = int(choice)

            # Problem Activity 1
            if choice == 1:
                print(
                    """
                      Welcome to problem activity #1
                    """
                    )
                
                # Delay for readability
                time.sleep(0.9)
                
                # Defining stocks at given times with a tuple
                stock_prices = [
                        ('09:00', 100.00),
                        ('09:30', 102.50),
                        ('10:00', 105.25),
                        ('10:30', 103.75),
                        ('11:00', 101.80),
                        ('11:30', 99.50),
                        ('12:00', 98.00)
                        ]   

                # Defining the function
                def analyze_stocks(stock_prices):
                    
                    # Creating new objects
                    highest_price = float('-inf')
                    lowest_price = float('inf')
                    total_price = 0
                    start_time = None
                    end_time = None
                    
                    for time, price in stock_prices:
                        # Check for highest price
                        if price > highest_price:
                            highest_price = price
                            highest_time = time

                        # Check for lowest price
                        if price < lowest_price:
                            lowest_price = price
                            lowest_time = time

                        # Update total price
                        total_price += price

                        # Update start and end time
                        if start_time is None:
                            start_time = time
                        end_time = time

                    # Calculate average price
                    average_price = total_price / len(stock_prices)

                    # Calculate total trading duration
                    start_hour, start_minute = map(int, start_time.split(':'))
                    end_hour, end_minute = map(int, end_time.split(':'))
                    total_trading_hours = end_hour - start_hour + (end_minute - start_minute) / 60

                    # Print results
                    print("Highest Price: ${:.2f} at {}".format(highest_price, highest_time))
                    print("Lowest Price: ${:.2f} at {}".format(lowest_price, lowest_time))
                    print("Average Price: ${:.2f}".format(average_price))
                    print(f"Total Trading Duration: {int(total_trading_hours)} hours".format(total_trading_hours))
                    

                    
                # Calling the analyze_stocks function
                analyze_stocks(stock_prices)
            # Problem Activity 2
            elif choice == 2:
                print(
                    """
                      Welcome to problem activity #2
                    """
                    )
                
                # Delay for readability
                time.sleep(0.9)
                
                # User input for custom phrase
                input_text = input("Please enter your phrase here: ")
                
                def remove_punctuation(text):
                    # Define punctuation marks
                    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

                    # Remove punctuation
                    text_without_punctuation = ''
                    for char in text:
                        if char not in punctuation_marks:
                                text_without_punctuation += char
                    return text_without_punctuation

                def word_frequency_counter(text):
                    # Remove punctuation and split the text into words
                    words = remove_punctuation(text).lower().split()

                    # Count the frequency of each word
                    word_freq = {}
                    for word in words:
                        word_freq[word] = word_freq.get(word, 0) + 1
                    return word_freq

                # Call the function with example text
                word_freq = word_frequency_counter(input_text)
                
                # Print result
                print(word_freq)
                
                # Delay for readability
                time.sleep(0.9)

            # Problem Activity 3
            elif choice == 3:
                print(
                    """
                      Welcome to problem activity #3
                    """
                    )
                
                # Delay for readability
                time.sleep(0.9)
                
                #User input for both lists
                list1_input = input("Please enter your numbers for set 1 here separated by commas: ")
                list2_input = input("Please enter your numbers for set 2 here separated by commas: ")
                
                def find_common_elements(list1, list2):
                    # Convert lists to sets
                    set1 = set(list1)
                    set2 = set(list2)

                    # Find common elements using set intersection
                    common_elements = set1.intersection(set2)

                    return common_elements

                # Example Input
                list1 = [int(i) for i in list1_input.split(",") if i.strip().isdigit()]
                list2 = [int(i) for i in list2_input.split(",") if i.strip().isdigit()]

                # Find and print common elements
                common_elements = find_common_elements(list1, list2)
                print("Common Elements:", common_elements)
                
                # Delay for readability
                time.sleep(0.9)

            # Exit program
            elif choice == 4:
                print(
                    """
                        You have exited the program\n
            =====================================================
                    """
                    )
                break

            # Invalid menu selection
            else:
                print("Invalid selection. Please enter a number between 1 and 4.")

        # Invalid user input
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

        # Delay for readability
        time.sleep(0.9)

# Program execution
program_project_5()