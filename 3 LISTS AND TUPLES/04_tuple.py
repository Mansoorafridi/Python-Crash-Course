# Immutable and Ordered:

# Tuples are immutable, meaning once they are created, their content cannot be changed.
# They maintain the order of elements based on their insertion.
# Example:

tup = (1, 2, 3)
print(tup[0])  # Immutable: Cannot modify elements

# Use Case: Tuples are handy for representing fixed collections of items, like coordinates (x, y)
# or dimensions (width, height), where the data should not cha





a =(1,2,4,6,"apple","orange",True)
print(a)
print(type(a))

b = ("apple")
print(type(b))          # we cant make a tuple having one element without ,

b1 = (1,)
print(type(b1))         # we use , for a single element in tuple

c = ()
print(c)          # empty tuple
