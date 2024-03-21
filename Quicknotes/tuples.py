# Tuple a collection which is ordered and unchangeable. Allows duplicate members!
# Tuples use paranthesis
# Tuples are faster than lists
# Tuples can have on value which requires a comma at the end
# Tuples can contain strings, integers and even lists within them

mixed_objects = ("Hello", [1, 2], 3)
one_number = (1,)
numbers = (0, 1, 2, 3)
print(mixed_objects)
print(numbers)
print(one_number)

# Slicing tuples
# we can slice tuples by using the colon symbole
# This will extract starting from 2 and the cutoff is the 6th index
print(numbers[2:6])
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[1:4])
print(letters[1:])
print(letters[::1])
print(numbers[2:4])
print(sorted(numbers))

# We can use the tuple constructor to create tuples

t = tuple(['me', 'you'])
print(t)
one_word = tuple("hello")
print(one_word)

# we can create tuples from dictionaries as well

td = tuple(dict(a=2, b=2))
print(td)

# we can use the count and index methods for tuples
count_test = (1, 2, 2, 2, 3, 4, 5, 6, "a")
print(count_test.count(2))
print(count_test.count("a"))
print(count_test.index(3))