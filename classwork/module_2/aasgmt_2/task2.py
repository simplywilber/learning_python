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

new_month = months.index(month_input) + 1
print(f'The date is: {new_month}/{day}/{year}')