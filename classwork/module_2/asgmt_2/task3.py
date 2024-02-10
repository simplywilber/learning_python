# Problem Activity 3:
# Write a program to give a student’s final grade in a course with the following grading
# scheme: there are two quizzes worth 100 points each, a midterm worth 100 points, and a
# final exam worth 100 points. 
# 
# The grade is based on the following weights: 
# 50% on the final exam, 
# 25 % on the midterm,
# and 25% on the quiz average. 
# 
# The grade is determined from
# the weighted in the traditional way: 
# 90 or over is an A, 
# below 90 down to 80 is a B, 
# below 80 down to 70 is a C, 
# below 70 down to 60 is D, 
# and below 60 is an F. 
# 
# The passing character
# grade is a C. Display a remark if it Passed or Failed.

quiz1 = int(input("Please enter the first quiz score: "))
quiz2 = int(input("Please enter the second quiz score: "))
quiz_average = ((quiz1 + quiz2) // 2)

midterm_grade = int(input("Please enter the midterm score: "))

final_exam_grade = int(input("Please enter the final exam score: "))

final_grade = int(quiz_average * .25) + int(midterm_grade * .25) + int(final_exam_grade * .50)

# Letter grade if statement
if final_grade >= 90 and final_grade <= 100:
    letter_grade = "A"
elif final_grade < 90 and final_grade >= 80:
    letter_grade = "B"
elif final_grade < 80 and final_grade >= 70:
    letter_grade = "C"
elif final_grade < 70 and final_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
    
# Final remark if statement
if letter_grade == "A" or "B" or "C":
    remark = "Passed"
else:
    remark = "Failed"   


print(f"The quiz average is: {quiz_average}")
print(f"The final average is: {final_grade}")
print(f"Letter grade: {letter_grade}")
print(f"Remark: {remark}")