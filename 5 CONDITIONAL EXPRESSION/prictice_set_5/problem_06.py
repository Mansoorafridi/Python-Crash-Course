#  Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

Marks = int(input("Enter your marks: "))

if (Marks >100 or Marks <0):
    grade = "invalid marks"

elif(Marks >=90):
    grade = "Excellent"

elif(Marks >=80):
    grade = "A"

elif(Marks >=70):
    grade = "B"

elif(Marks >=60):
    grade = "C"

elif(Marks >=50):
    grade = "D"

else:
    grade = "Fail"

print(grade)
