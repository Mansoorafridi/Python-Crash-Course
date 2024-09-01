# # What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
t = len(s)
print(t)

a = {1,2,3,4,5,5.0}     # # its length will be 5 because in python;  in Python, the integer 5 and the
                        # # floating-point number 5.0 are treated as the same value when it comes
                        #  to set membership. it also apply to dictionary.
                        # # Therefore, the set will contain only one instance of this value. 
print(len(a))

