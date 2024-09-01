# Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f (user):
    return (user * (9/5)) + 32.      ## formula to convert Celsius to Fahrenheit (celsius x (9/5) + 32.
user = int(input("Enter temperature in celsius: "))
print(f"{c_to_f(user)} °F")
