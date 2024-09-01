# Mutable and Ordered:

# Lists are mutable, meaning you can change their content after they are created.
# They maintain the order of elements based on their insertion.
# Example:

lst = [1, 2, 3]
lst.append(4)  # Mutable: Can add elements
print(lst)     # Ordered: Prints [1, 2, 3, 4]

# Use Case: Lists are useful when you need to store and manipulate collections of items where the order
#  matters, such as maintaining a sequence of steps in a process.

friends= ["Apple", "Grips", "orange", 7,False]
print(friends[0])

print(friends[0:4:2])    # [7,9] list sliciing

friends[0]= "Grips"      

print(friends)

l1 = [7,9,"apple"]
print(l1[0])