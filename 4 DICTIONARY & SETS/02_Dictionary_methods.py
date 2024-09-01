my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.items())   # items(): Returns a list of (key,value)in form of tuples.
                         # output = dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])


print(my_dict.keys())    # keys() give us only keys
                        # output = (['name', 'age', 'city'])

print(my_dict.values()) # values() give us onle values of keys 
                        # output = (['Alice', 30, 'Ney York'])

my_dict.update({"age": 31}) # update() update age = 31
print(my_dict)

print(my_dict.get("name")) # output = Alice
