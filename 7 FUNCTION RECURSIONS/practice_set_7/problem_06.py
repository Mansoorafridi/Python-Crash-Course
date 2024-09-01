#   Write a python function to print multiplication table of a given number.
user = int(input("Enter a number: "))

def table():
    for i in range(1,11):
     print(f"{user} x {i} = {user*i}")

table()





user = int(input("Enter a number: "))

def multiply():
    i = 1
    while i <=10:
        print(f"{user} x {i} = {user*i}")
        i += 1

multiply()

