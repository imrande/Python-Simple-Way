from time import sleep

class Test:
    def __init__(self):
        print('Constructor')
    
    def __del__(self):
        print('Destructor')

t1 = [Test(), Test(), Test()] # 3 time __init__ will be called
print('Making list object for GC')
del t1 # 3 times __del__ will be called
sleep(3)
print('End of application')