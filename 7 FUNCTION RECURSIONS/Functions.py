def multiply():
    a = 2
    b = 4
    return a * b
print(multiply())  # Output: 8
print(multiply())  # Output: 8

## if we want to change the values of a and b when we call a function we will use parameters.

def sum(a,b):       ## a and b are parameters
    print(a+b)

sum(2,4)            ## 2 and 4 are arguments
sum(8,10)

                ## OR

                
##      ##      ##      ##      ##
def user(name):         ## name is parameter
    print("Good day," + name)

user("jonathan")        ## jonathan and jhon are arguments
user("jhon")


##      ##      ##      ##      ##
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    print(average)

avg()