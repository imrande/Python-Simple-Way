# whenever an exception occurs pvm will create the corresponding exception 
# object and check for handling code. 
# if available then it will be executed and rest of program normally.
# if it isn't available then pvm terminates the program and print corresponding errors

try:
    print('Hello')
    print(10 / 0)
except ZeroDivisionError:
    print('Divide by zero')
finally:
    print('Hola')

print('Que tenga')

#