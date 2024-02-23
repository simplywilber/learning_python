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
    
    num = int(input("           Please enter your numbers here: "))
    
    input_list = []
    user_list = []
    
    for n in ranged_num:
        nlist.append(n)
    print(nlist)



elif choice == 2:
    print(
        """
            Welcome to problem activity #2
        """
          )
    num = int(input("           Please enter your number here: "))

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


