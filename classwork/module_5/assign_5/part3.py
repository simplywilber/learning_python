def find_common_elements(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find common elements using set intersection
    common_elements = set1.intersection(set2)

    return common_elements

# Example Input
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find and print common elements
common_elements = find_common_elements(list1, list2)
print("Common Elements:", common_elements)