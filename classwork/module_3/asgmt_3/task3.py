# Write a python program that prints 1 2 4 8 16 32 ...n2 and the sum of the
# sequence number.
import math

n_input = int(input("Please enter the value of n: "))

n_range = range(n_input)

ret = []

sum = 0

# Squares each integer within the sequence
for n in n_range:
    ret.append((n+1) ** 2)

# Finds the sum of all newly squared numbers
for x in ret:
    sum += x


print(f"The sequence of n is: {ret}")
print(f"The sum of the sequence is: {sum}")
