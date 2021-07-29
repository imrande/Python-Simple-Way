# by default garbage collection is enable but we can disable it requirement purpose
# main purpose of gc is destroy unnecessary object
# gc always call __del__ method before destroy object for cleanup activities

import gc
from time import sleep

print(gc.isenabled()) # True
gc.disable() # return None
print(gc.isenabled()) # False
gc.enable()
print(gc.isenabled()) # True

class Test:
    def __init__(self):
        print('Object is created')
    
    def __del__(self):
        print('Deestroying object')

# t = Test()
# t = None
# sleep(10)
# print('End of application')

# after control reaches end of code gc deletes all object by default
t3 = Test()
t4 = Test()
print('Aha!')

""" output =>
Object is created
Object is created
Aha!
Deestroying object
Deestroying object
"""