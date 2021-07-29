try:
    print("Outer try block") # 1
    try:
        print("Inner try block") # 2
        print(10 / 0)
    except ZeroDivisionError:
        print("Inner except block") # 3
    finally:
        print("Inner finally block") # 4 
except:
    print("Outer except block")
finally:
    print("Outer finally block") # 5

# Case 2
try:
    print("Outer try block") # 1
    try:
        print("Inner try block") # 2
        print(10 / 'two')
    except ZeroDivisionError:
        print("Inner except block") 
    finally:
        print("Inner finally block") # 3 
except:
    print("Outer except block") # 4
finally:
    print("Outer finally block") # 5

# Case 3
try:
    print('Outer try block') # 1
    print(10 / 0)
    try:
        print('Inner try block')
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block')
except:
    print('Outer except block') # 2
finally:
    print('Outer finally block') #3