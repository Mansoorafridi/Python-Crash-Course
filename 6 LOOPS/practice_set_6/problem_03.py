##  Attempt problem 1 using while loop.
##  Problem 1:
## Write a program to print multiplication table of a given number using for loop.

user = int(input("Enter a number: "))
i = 1
while i<=10 :
    print(user*i)       ## simple way
    i += 1      

user = int(input("Enter a number: "))
i = 1
while i<=10 :
    print(f"{user}x{i}={user*i}")       ## good way
    i += 1