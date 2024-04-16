while True:
    # Initial user input
    user_input = input("Please enter your list of integers: ")
    integers_list = [int(i) for i in user_input.split() if i.strip().isdigit()]

    # Check if the number of inputs exceeds 9
    if len(integers_list) > 9:
        print("Too many inputs, please try again")
    else:
        # Find the middle item
        middle_index = len(integers_list) // 2
        middle_item = integers_list[middle_index]
        print(f"The middle item is: {middle_item}")
        break  # Exit the loop if the input is within limits