# 3 important questions about GC

## difference between `del t1` and `t1 = None`

### del t1

t1 will be deleted and corresponding object will be eligible for garbage collection.

```py
class Test:
    def __init__(self): print('Constructor')
    def __del__(self): print('Destructor')

t1 = Test() # Constructor
del t1 # Destructor
print('End of program') # End of program
```

If we don't want object and corresponding ref variable then we'll have to use this approach

### t1 = None

t1 is now pointing None object and object (Test()) will be eligible for garbage collection.

```py
class Test:
    def __init__(self): print('Constructor')
    def __del__(self): print('Destructor')

t1 = Test() # Constructor
t1 = None # Destructor
print('End of program') # End of program
```

If we don't want object and want to keep ref variable then we'll have to use this approach

## How to find number of references in object

```py
import sys

class Test:
    pass

t1 = Test()
print(sys.getrefcount(t1)) # 2 [t1, self]

m1 = Test()
m2 = m1
m3 = m2
m4 = m3
print(sys.getrefcount(m3)) # 5
```

## Difference between constructor and destructor

| Constructor      | Destructor |
| ----------- | ----------- |
| name is always `__init__()`      | name is always `__del__`       |
| It is initialized instance variables   | It is meant for cleanup(resource de-allocation of object)  activities      |
| After creating object constructor automatically executed   | Just before gc destroy object called destructor       |