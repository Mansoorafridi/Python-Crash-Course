'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n x n-1 x.....3 x 2 x 1
factorial(n) = n * factorial(n-1)          ## Formula

example factorial of 5
factorial(5)
2 x 1 = 2
3 x 2 = 6
4 x 6 = 24
5 x 24 = 120
'''
def factorial(n):
    if n==1 or n==0:        # Base case
        return 1
    else:
        return n * factorial(n-1)       # Recursive case

n = int(input("Enter a number: "))
print(factorial(n))
