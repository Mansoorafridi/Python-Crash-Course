# # Create an empty dictionary. Allow 4 friends to enter their name as "Enter yor favorite language: " 
# # value and use key as their names. Assume that the names are unique.

# Create an empty dictionary
name = {}

# Allow 4 friends to enter their name and favorite language
user1 = input("Enter your name: " )
user1_language = input("Enter your favorite language: ")

user2 = input("Enter your name: " )
user2_language = input("Enter your favorite language: ")

user3 = input("Enter your name: " )
user3_language = input("Enter your favorite language: ")

user4 = input("Enter your name: " )
user4_language = input("Enter your favorite language: ")

# Add the entries to the dictionary

name.update({user1: user1_language})
name.update({user2: user2_language})
name.update({user3: user3_language})
name.update({user4: user4_language})

# Print the dictionary
print(name)



