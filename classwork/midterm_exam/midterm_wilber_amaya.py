# Wilber Amaya-Maurisio Midterm Exam in Python Programming

# Create a list of numbers
mynumbers = [5, 10, 8, 7, 20, 18, 2, 9]

# 1. Append an item to the list
mynumbers.append(6)
print(f"#1. After appending 6: {mynumbers}")

# 2. Extend the list with another list
more_numbers = [13, 14, 15]
mynumbers = [5, 10, 8, 7, 20, 18, 2, 9]
mynumbers.extend(more_numbers)
print(f"#2. After extending with more numbers: {mynumbers}")

# 3. Insert an item at a specific position
mynumbers.insert(3,10)
print(f"#3. After inserting 10 at index 3: {mynumbers}")

# 4. Remove the first occurence of an item
mynumbers.remove(7)
print(f"#4. After removing the first occurrence of 7: {mynumbers}")

# 5. Pop an item from the list
mynumbers.pop(10)
print("#5a. Popped items: 15")
print(f"#5b. After popping: {mynumbers}")

# 6. Reverse the list
mynumbers.reverse()
print(f"#6. After reversing: {mynumbers}")

# 7. Sort the list
mynumbers.sort()
print(f"#7. After sorting: {mynumbers}")

# 8. Count the occurrence of an item
count = mynumbers.count(10)
print(f"#8. Count of 10: {count}")

# 9. Maximum values in the list
max = max(mynumbers)
print(f"#9. Maximum number of element: {max}")

# 10. Minimum values in the list
min = min(mynumbers)
print(f"#10. Minimum number of element: {min}")

# 11. Copy the numbers of the list
n_list = [5, 10, 8, 7, 20, 18, 2, 9]
mynumbers = n_list.copy()
print(f"#11. Copy the list numbers of elements: {mynumbers}")

# 12. Sum the numbers element
sum = sum(mynumbers)
print(f"#12. The sum of the numbers: {sum}")\

# 13. Length of the list
length = len(mynumbers)
print(f"#13. The total length of the elements: {length}")

# 14. Clear the occurrence of an item
mynumbers.clear()
print(f"#14. After clearing the list: {mynumbers}")