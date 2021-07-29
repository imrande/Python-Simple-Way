# Equality operators (==)

"""
Rules =>
1) no. of elements must be same
2) content must be same (case sensitive)
3) order must be same
"""

l1 = ['Dog', 'Cat', 'Rat']
l2 = l1
l3 = [x.upper() for x in l1]
l4 = ['Cat', 'Dog', 'Rat']

print(l1 == l2) # True
print(l1 == l3) # False
print(l1 == l4) # False

# Membership operators (in, not in)
print(10 in [10, 20]) # True
print(100 not in [10, 2000]) # True

# Realtional operators (<, >, <=, >=) [works with set, list, tuple, str]
# it compares element ith index to another list's ith index
l1 = list(range(10, 50, 10))
l2 = list(range(50, 70, 10))

print(l1 < l2) # True [10 < 50]
print(l1 <= l2) # True [10 <= 50]
print(l1 > l2) # False [10 > 50]
print(l1 >= l2) # False [10 >= 50]

# list_1 contains values more than list_2 that's why list_1 is greater or vice versa
list_1 = [10, 20, 5]
list_2 = [10, 20]
print(list_1 < list_2) # False
print(list_1 > list_2) # True

list_1 = {'x': 50}
list_2 = {'y': 40}
print(list_1.items() < list_2.items()) # False
# print(list_1.values() < list_2.values()) => TypeError
print(list_1.keys() < list_2.keys()) # False