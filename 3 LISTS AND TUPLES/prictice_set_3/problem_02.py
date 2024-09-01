# # Prompt the user to enter their marks.

student1 = int(input("Enter your marks:"))
student2= int(input("Enter your marks:"))
student3 = int(input("Enter your marks:"))
student4 = int(input("Enter your marks:"))
student5 = int(input("Enter your marks:"))
student6 = int(input("Enter your marks:"))

# # Store the marks in a list named result.

result = [student1,student2,student3,student4,student5,student6]
# # use sort method on list named result to show result sorted way.

result.sort()
print("Marks",(result))
