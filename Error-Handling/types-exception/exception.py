# 2 types of exception :-
# predefined exception
	# known as inbuilt exception.
	# These will be raised automatically by python virtual machine whenever a
	# particular event occurs [TypeError, ZeroDivisionError etc]
# user defined exception [programmer defined]

class NumberError(Exception):
    def __init__(self):
        message = 'number too young'
        super().__init__(message)

x = 10
y = 20

if x < y:
	raise NumberError
