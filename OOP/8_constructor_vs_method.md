# Difference between Constructor and Method

## Constructor

- Constructor name should be always __init__()
- Constructor will be executed automatically whenever we're creating an object.
- Per object constructor will be executed only one time.
- Main purpose of constructor is to declare and initialize instance variables.

## Method

- Method name can be any Identifier
- Method doesn't call implicitly, we have to call it explicitly.
- We can invoke method as many times as we want per object.
- Inside method we write business logic based on programming requirement.

### What happends if we provide method name same as class name

yes, it is valid in python but not recommended

```py
class Test(object):
	def Test(self):
		print('Test Method')

t = Test() # Constructor called
t.Test() # Method Invoked
```