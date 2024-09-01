## List Concatenation (+)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Adding two lists
Combined_list = list1 + list2
print(Combined_list)        # output = [1, 2, 3, 4, 5, 6]

## List Repetition (*)

list = [1, 2, 3]
repeated_list = list * 2
print(repeated_list)        # output = [1, 2, 3, 1, 2, 3]

## List Slicing (:)

list1 = [1, 2, 3, 4, 5]
slicing = list1[1:4]        # slicing from index 1 to 4 (4 is not include)
print(slicing)

## Liist Membership (in)

list1 = [1, 2, 3, 4, 5]
print(3 in list1)           # output = True
print(5 in list1)           # output = True

## List Length (len())

list1 = [1, 2, 3, 4, 5]
print(len(list1))           # output = 5

## Accessing List element By Index

friends= ["Apple", "Grips", "orange", 7,False]
print(friends[0])          # output = Apple

print(friends[0:4:2])    # output = [Apple,orange] list sliciing

friends[0]= "Grips"      # insert Grips at index 0
print(friends)

