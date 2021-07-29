# print the exception in the console

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print('Exception type is',type(error))  # <class 'ZeroDivisionError'>
    print(error)
    print(error.__class__)  # <class 'ZeroDivisionError'>
    print(error.__class__.__name__)  # ZeroDivisionError
    print(error.__doc__)  # it will print the docstring inside the class
