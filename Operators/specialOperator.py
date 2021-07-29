# special operator in python
# identity operator (is, is not)
# membership operator (not in, in)

a = 10
b = 10
print(a is b) # True
print(a is not b) # False

# if operands of both side point to same object then `is` return True
a = 'durga'
b = 'Durga'.lower()

print(a is b) # False
print(a is not b) # True
a = b = 'durga'
print(a is b) # True
print(a is not b) # False

l1 = list(range(10, 50))
l2 = list(range(10, 50))
print(l1 is l2) # False
print(l1 is not l2) # True
print(l1 == l2) # True

# membership operator
# value in sequence (any iterable object)

print('===================')
s = 'hello learning python is very easy'
print('h' in s) # True
print('h' not in s) # False
print('d' in s) # False
print('d' not in s) # True

l = ['sunny', 'bunny', 'jenny', 'jimmy']
print('sunny' in l) # True
print('bunny' in l) # True
print('j' in l[2]) # True
print('pinky' in l) # False