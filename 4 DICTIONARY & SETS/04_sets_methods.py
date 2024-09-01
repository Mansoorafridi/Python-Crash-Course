fruites = {"apple", "banana", "cherry"}

# Adding an item
fruites.add("orange")
print(fruites) 

# Removing an item
fruites.remove("apple")
print(fruites) 

# Deleting a random item
fruites.pop()       # randomly deltes an item
print(fruites) 

# Clear ()
fruites.clear()
print(fruites) 

a = {1,2,3,5,9,6}
b ={1,3,9,10,11,12}

print(a.union(b))
print(a.intersection(b))
