# Create an empty dictionary
student_grades = {}




# Create our input prompt
grade_prompt = "Enter name and grade: "

# Create a delete prompt biased on the student's name
del_prompt = "Enter a name to delete: "

# Create the menu
menu_prompt=("1. Add/Modify student grade\n"
             "2. Delete student grade\n"
             "3. Print student grade\n"
             "4. Quit\n")

# Runs the program
while True: # exit when user enters no input
    command = input(menu_prompt).lower().strip()
    
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    elif command == '2':
        name = input(del_prompt)
        del student_grades[name]
    elif command == '3':
        print(student_grades)
    elif command == '4':
        break
    else:
        print("Invalid command, please try again")
        




