# string slicing
# it is used to get a part of the string

name = "jonathan "           # every character in string called index
                            # index: 0 1 2 3 4 5 6 7    -8 -7 -6 -5 -4 -3 -2 -1
                            # string:j o n a t h a n    j   o  n  a  t  h  a  n


shortname = name[0:3]         # start from the index 0 all the way to index 3 excluding 3.
character1 = name [1]         # to get a specific character
shortname1 = name [1:5]
print(shortname)
print(character1)
print(shortname1)
print(name[1:6])
print(name[-6:-2])
