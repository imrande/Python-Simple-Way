# which may raise an exception is called risky code
# risky code only inside try block [best practice]

print('Hello')
try:
    print(10 / 0) # risky code
except ZeroDivisionError as e:
    print(e) # handling errors / alternative way
finally:
	print('Hola')
