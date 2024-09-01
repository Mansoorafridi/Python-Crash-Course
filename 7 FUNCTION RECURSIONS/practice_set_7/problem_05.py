#  Write a python function which converts inches to cms
def centimeters():
    return 2.54 * inches

inches = int(input("Enter length in inches: "))
print(f"{inches} is equal to {centimeters()} cm")
