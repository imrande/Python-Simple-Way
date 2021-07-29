# We can pass a function as arguments to another function

def takeArgsAsFunction(func):  func() # Hello
def f2(): print('Hello')
takeArgsAsFunction(f2)