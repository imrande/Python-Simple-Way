# function is an object
# function name is an ref variable which is pointing function object

# we can give another name of the existing function, which is called function aliasing...
# even if we delete one ref we can still call object by another reference

def f1(): print('Hello')

print(id(f1))
print(id(f1()))
print(f1)

def wish(name:str):
	print(f'Hello, {name}')

greeting = wish
greeting('Alina')
wish('Maina') # Hello, Maina
print(id(greeting) == id(wish)) # True

del wish
greeting('Laila') # Hello, Laila
