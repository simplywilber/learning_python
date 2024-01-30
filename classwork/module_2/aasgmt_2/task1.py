# Problem Activity #1
# Make a program that would input five test scores and output the highest score,
# the lowest score and average score.
# Enter five test scores:
# Highest score:
# Lowest Score:
# Average Score:

test1 = int(input("Please type the first test score here: "))
test2 = int(input("Please type the second test score here: "))
test3 = int(input("Please type the third test score here: "))
test4 = int(input("Please type the fourth test score here: "))
test5 = int(input("please type the fifth test score here: "))

if test1 > test2 and test1 > test3 and test1 > test4 and test1 > test5:
    print(f"The highest score is: {test1}")
elif test2 > test1 and test2 > test3 and test2 > test4 and test2 > test5:
    print(f"The highest score is: {test2}")
elif test3 > test1 and test3 > test2 and test3 > test4 and test3 > test5:
    print(f"The highest score is: {test3}")
elif test4 > test1 and test4 > test2 and test4 > test3 and test4 > test5:
    print(f"The highest score is: {test4}")
else:
    print(f"The highest score is: {test5}")
    
if test1 < test2 and test1 < test3 and test1 < test4 and test1 < test5:
    print(f"The lowest score is: {test1}")
elif test2 < test1 and test2 < test3 and test2 < test4 and test2 < test5:
    print(f"The lowest score is: {test2}")
elif test3 < test1 and test3 < test2 and test3 < test4 and test3 < test5:
    print(f"The lowest score is: {test3}")
elif test4 < test1 and test4 < test2 and test4 < test3 and test4 < test5:
    print(f"The lowest score is: {test4}")
else:
    print(f"The lowest score is: {test5}")
    
average_score = (test1 + test2 + test3 + test4 + test5) // 5
print(f"The average score is: {average_score}")