# Task 3
# Write a Python program to give student’s final grade in a course
# with the following grade scheme: there are three quizzes worth 
# 10 point each, a midterm worth 100 points, and final worth 100 
# points. The grade is based on the following weights: 50% on the 
# final exam, 25% on the midterm exam, and 25% on the quiz 
# average. (Be sure to normalize the quiz average to 100 by 
# multiplying by 10).

# Inputs for all three quizzes as integers
quiz1 = int(input("Enter quiz one's score here: "))
quiz2 = int(input("Enter quiz two's score here: "))
quiz3 = int(input("Enter quiz three's score here: "))

# Input for midterm 
midterm_exam = int(input("Enter midterm exam score here: "))

# Input for final exam
final_exam = int(input("Enter final exam score here: "))

# Finding the quiz average and normalizing to 100
quiz_average = ((quiz1 + quiz2 + quiz3) / 30) * 100

# Finding the final grade based on the given weights
final_grade = (quiz_average * 0.25) + (midterm_exam * 0.25) + (final_exam * 0.5)

# Final outputs
print(f"The quiz average is: {quiz_average}%")
print(f"The final grade is {final_grade}")




