secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

num = int(input("Your number here"))

while num != 0:
    if num != 777:
        print("Ha ha! You're stuck in my loop!")
    elif num == 777:
        print("Well done, muggle! You are free now.")
        break
