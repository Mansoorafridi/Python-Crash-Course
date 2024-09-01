# Mutable: you can modify a set by adding or removing items.
# Unordered: The item in a set do not have a defined ordered.
# Unique items: No two items can be same.

fruites = {"apple", "banana", "cherry"}

# Trying to add a duplicate item
fruites.add("apple")            # output will be same {"apple", "banana", "cherry"} in any order
print(fruites)

# Adding an item
fruites.add("orange")
print(fruites)          # it can be in any order eg {"cherry", "banana", "apple", "orange"}
