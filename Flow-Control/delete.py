# del is used in python to delete variables

# del vs immutable objects
s = 'durga'
s2 = s
s3 = s2
del s # it just deleted s but other variables still point to durga object
# print(s) NameError, since s is deleted
# del s2[0] TypeError [because of immutability]
print(s2, s3)

# del vs None
# after del we can't use that variables but after assigning None we can use variable

s = 'Imran'
del s
# print(s) NameError
s1 = None
print(s1) # None

