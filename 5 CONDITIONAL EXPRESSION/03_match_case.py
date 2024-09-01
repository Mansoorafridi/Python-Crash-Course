# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

dayes_of_the_week = input("What day is today: ")

match dayes_of_the_week:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday" | "Sunday":
        print(True)
    
    case _:
        print(False)

age = int(input("Enter your age: "))

match age:
    case _ if age <= 17:
        print("You cannot cast the vote")

    case _:                                 # case _ exactly works like else
        print("You can cast the vote")
