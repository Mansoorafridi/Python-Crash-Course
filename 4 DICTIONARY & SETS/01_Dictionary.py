# Empty dictionary
my_dict = {}

# Dictionaries are mutable, allowing for the addition, modification, and deletion of key-value pairs.

d = {'a': 1, 'b': 2}
d['c'] = 3     # Mutable: Can add/update elements
print(d)       # Ordered: Prints {'a': 1, 'b': 2, 'c': 3}

# Dictionary with initial values
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30


# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating an existing value
my_dict["age"] = 31

print(my_dict)
