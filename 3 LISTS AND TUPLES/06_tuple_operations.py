## Basic operations

## Tuple Concatenation (+)

Tuple1 = (1, 2, 3)
Tuple2 = (4, 5, 6)
# Adding two Tuple
Combined_Tuple = Tuple1 + Tuple2
print(Combined_Tuple)        # output = (1, 2, 3, 4, 5, 6)

## Tuple Repetition (*)

Tuple = (1, 2, 3)
repeated_Tuple = Tuple * 2
print(repeated_Tuple)        # output = (1, 2, 3, 1, 2, 3)

## LTuple Membership (in)

Tuple1 = (1, 2, 3, 4, 5)
print(3 in Tuple1)           # output = True
print(5 in Tuple1)           # output = True

## Tuple Length (len())

Tuple1 = (1, 2, 3, 4, 5)
print(len(Tuple1))           # output = 5


## Accessing Tuple element By Index

friends= ("Apple", "Grips", "orange", 7,False)
print(friends[0])          # output = Apple

print(friends[0:4:2])    # output = (Apple,orange) list sliciing
