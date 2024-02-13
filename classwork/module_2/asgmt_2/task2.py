# Problem Activity #2:
# Write a program that accepts dates written in the usual way and then outputs
# them as three numbers.
# Sample Input:
# September 14, 2023
# Output:
# The date is: 9/14/23

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_input = input("Please enter the month here: ")
day = input("please enter the day here: ")
year = input("Please enter the year here: ")

# Month name interger coversion if statement
if month_input == "January":
    new_month = 1
elif month_input == "February":
    new_month = 2
elif month_input == "March":
    new_month = 3
elif month_input == "April":
    new_month = 4
elif month_input == "May":
    new_month = 5
elif month_input == "June":
    new_month = 6
elif month_input == "July":
    new_month = 7
elif month_input == "August":
    new_month = 8
elif month_input == "September":
    new_month = 9
elif month_input == "October":
    new_month = 10
elif month_input == "November":
    new_month = 11
elif month_input == "December":
    new_month = 12

# Final output
print(f'The date is: {new_month}/{day}/{year}')