
# declaring variables
username = ["Jerico", "Wilber"]
user_pw = ["Estella", "Amaya"]
x = 0
attempts = 3
def Capitalization_Correction():# function to quickly call it multiple times
    sentence = input("Enter a sentence up to 50 characters: ")
    if len(sentence) > 50:
        print("Your sentence has more than 50 characters")
        return  # returns to selection
    fixed_sentence = sentence.capitalize()  # Capitalizes first word in the sentence and lowers the rest
    if fixed_sentence[-1] not in ['.', '!', '?']:  # checks for end punctuation if not add period as default
        fixed_sentence += '.'  # adds period
    for i in range(len(fixed_sentence)-1):  # capitalizes after a punctuation
        if fixed_sentence[i] in ['.', '!', '?']:
            fixed_sentence = fixed_sentence[:i + 2] + fixed_sentence[i + 2:].capitalize()
            # uncomment for the process
            # print("Punctuation: ", fixed_sentence[i])
            # print("after punctuation: ", fixed_sentence[:i + 2], fixed_sentence[:i + 2], "\n", fixed_sentence[i + 2:])
    print("\n\nCorrection: " + fixed_sentence)

while attempts > 0:  # while attempts greater than 5, continue
    attempt = f"""\n    You have {attempts-1} attempts left."""  # formatting for when user failed login
    username_input = input("""
        Enter username: """
                           )  # user inputs Username
    userpw_input = input("""
        Enter Password: """
                         )  # user inputs Password
    if (username_input == username[0] and userpw_input == user_pw[0]) or (
            username_input == username[1] and userpw_input == user_pw[1]):  # authentication login.
        attempts = 0  # fix for exiting program
        print(f"""
            ==============================
                    Welcome, {username_input}
            ==============================""")
        # while x not equal 4, continue
        while x != '4':  # selection input
            print("""
            ==============================
                      Main Menu\n
              1) Enter 2 to begin problem #9\n
              2) Enter 4 to log out and exit\n
            ==============================\n""")
            x = input("Please enter your selection: ")
            if x == '2':
                Capitalization_Correction()  # calls the function
            elif x == '4':  # exits program
                print("""
            ==============================
                      Thank you!
            ==============================""")
                break
            else:
                print("Please enter 2 or 4.")
    else:
        attempts -= 1  # minus one after failed login
        if attempts > 0:
            print("\nIncorrect username or password.")
            print(attempt)
        else:
            print("\nPlease try again later.")

