friends= ["Apple", "Grips", "orange", 7,False]
friends.append ("jonathan")                     # adds jonathan at the end.

print(friends)

list = [1,3,36,22,19,33,50,2]
list.pop()                             # pop will delete last element on list.
                                       # or pop(3) will delete whatever is on index 3.
print(list)

list = [1,3,36,22,19,33,50,2]
list.remove(36)                             # it will remove 36 from list.
print(list)

list = [1,3,36,22,19,33,50,2]
list.sort()                                 # sort the list
print(list)

list = [1,3,36,22,19,33,50,2]
list.insert(3,50)                             # it insert 50 at index 3
print(list)

list = [1,3,36,22,19,33,50,2]
list.reverse()                                 # reverse the list
print(list)

# # sum a list of four numbers

a = [22,11,44,5]
print(sum(a))
