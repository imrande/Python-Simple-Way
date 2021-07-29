# by default module ran only one time when it is imported and after that if 
# anything is changed it won't reflect, so that's why reload module explictly
# with importlib.reload(name) function

import module2, time, importlib

module2.add(10,	20)
time.sleep(5)
importlib.reload(module2) 
module2.x()