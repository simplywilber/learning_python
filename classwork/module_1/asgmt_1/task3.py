# Task 3
# Write a Python program to give student’s final grade in a course
# with the following grade scheme: there are three quizzes worth 
# 10 point each, a midterm worth 100 points, and final worth 100 
# points. The grade is based on the following weights: 50% on the 
# final exam, 25% on the midterm exam, and 25% on the quiz 
# average. (Be sure to normalize the quiz average to 100 by 
# multiplying by 10).

quiz1 = int(input("Enter quiz one's score here:"))

quiz2 = int(input("Enter quiz two's score here:"))

quiz3 = int(input("Enter quiz three's score here:"))

quiz_average = (quiz1 + quiz2 + quiz3) * 10 // 3
print("The quiz average is:", quiz_average + "%")

quiz_total = int(float(quiz_average) * float(.25) * 10)


mideterm_exam = int(input("Enter midterm exam score here:"))
midterm_total = int(mideterm_exam * float(.25))

final_exam = int(input("Enter final exam score here:"))
final_exam_total = int(final_exam * float(.50))

final_grade = quiz_total + midterm_total + final_exam_total
print(f"The final grade is {final_grade}")




