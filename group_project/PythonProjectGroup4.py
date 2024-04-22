# initializing variables for user login
username = ["Jerico", "Wilber"]
user_pw = ["Estella", "Amaya"]
x = 0
attempts = 5


# function to quickly call the capitalization correction function multiple times
def Capitalization_Correction():
    sentence = input("\nEnter a sentence up to 50 characters: ")[:50]
    # Capitalizes first word in the sentence
    fixed_sentence = sentence.capitalize()
    # checks if there is no punctuation at end of sentence in list
    # if not then a period is set as default
    if fixed_sentence[-1] not in ['.', '!', '?']:
        fixed_sentence += '.'
        # checks for punctuation at end of sentence in list
        # then starts the sentence correction
    if fixed_sentence[-1] in ['.', '!', '?']:
        # this for loop adds a capital
        # for after in list and index is less than the length of fixed_sentence
        for i in range(len(fixed_sentence)):
            # if fixed sentence in list is true and index is less than
            # the length of the sentence -1 then use Capitalize
            if fixed_sentence[i] in ['.', '!', '?'] and i < len(fixed_sentence) - 1:
                # uses capitalize function from 2 at 2 after a punctuation
                fixed_sentence = fixed_sentence[:i + 2] + fixed_sentence[i + 2:].capitalize()
    print(f"\nCorrected sentence: {fixed_sentence}")


# while statements for attempts
while attempts > 0:
    attempt = f"""\n    You have {attempts} attempts left."""
    print(attempt)
    username_input = input("""
     Enter username: """
    )
    userpw_input = input("""
     Enter Password: """
    )
    # if statements for username and password
    if (username_input == username[0] and userpw_input == user_pw[0]) or (
            username_input == username[1] and userpw_input == user_pw[1]):
        attempts = 5
        print(f"""\n
==============================\n
        Welcome, {username_input}\n
==============================
        """)
        while x != '4':
            print("""
==============================\n
          Main Menu\n
  1) Enter 2 to begin problem #9\n
  2) Enter 4 to log out\n
==============================\n""")
            x = input("Please enter your selection: ")
            if x == '2':
                Capitalization_Correction()
            elif x == '4':
                print("""
==============================
          Thank you!
==============================""")
                x = 0
                break
        print("""
    Please try again Later.""")
    elif username_input == "" and userpw_input == "":
        print("""
Thank you for using sentence correction""")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("""
 Incorrect username or password.""")
        else:
            print("""
==============================\n
   Please try again later.\n
==============================
  """)
