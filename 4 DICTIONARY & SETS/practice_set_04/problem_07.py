# You cannot include a list (or any mutable type, like a dictionary) inside a set in Python.
# Sets require their elements to be hashable and immutable. Lists are mutable and therefore not hashable,
# so trying to include a list in a set will raise a TypeError.

# This will raise a TypeError:
# s = {8, 7, 12, "Harry", [1, 2]}
# print(type(s))

# Instead, you can use a tuple instead of a list, as tuples are immutable and hashable:
a = {1, 2, 118, "Jhon", (22, 25)}
print(type(a))
print(a)
