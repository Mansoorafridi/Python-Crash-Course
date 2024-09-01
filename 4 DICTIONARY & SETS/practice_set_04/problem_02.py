# Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

user1 = int(input("Enter the number: "))

user2 = int(input("Enter the number: "))

user3 = int(input("Enter the number: "))

user4 = int(input("Enter the number: "))

user5 = int(input("Enter the number: "))

user6 = int(input("Enter the number: "))

user7 = int(input("Enter the number: "))

user8 = int(input("Enter the number: "))
unique_numbers = {user1, user2, user3, user4, user5, user6, user7, user8}   # use of set

print("unique numbers: ",unique_numbers )
