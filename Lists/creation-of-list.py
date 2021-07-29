# we can create a list by different ways

# by using []
l = []
print(l) # []
print(type(l)) # list

# if we know already data
l = [4, 5, 6]
print(l) # [4, 5, 6]
print(type(l)) # list

# dynamically
l = eval(input('Enter list '))
print(type(l)) # list
print(l)

# by using list() function
l = list('string')
print(l) # ['s', 't', 'r', 'i', 'n', 'g']

# by using str.split() method
l = "Hello World".split()
print(l) # ['Hello', 'World']