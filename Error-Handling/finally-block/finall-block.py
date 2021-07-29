try:
    pass
    # risky code
except:
    pass
    # handling code
finally:
    pass
    # close the connection [put all cleanup code]

# case 0
try: print('try') # try
except: print('except')
finally: print('finally\n') # finally

# case 1
try:
    print('try') # try
    print(10 / 0)
except ZeroDivisionError as e: print(e) # error message
finally: print('I am done!\n') # I am done!

# case 2
try:
    print('Hello') # Hello
    print(10 / 'a')
# raise TypeError but before throw error finally will be executed
except ValueError as f: print(f)
finally: print('I am finished') # I am finished