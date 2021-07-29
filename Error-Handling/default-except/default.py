# except: default exception block

try:
    x, y = map(int, input().strip().split())
    print(x / y)
# default except block must be at the last otherwise pvm will raise SyntaxError
except:
    print('Provide valid input')