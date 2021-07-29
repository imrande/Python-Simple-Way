# difference between finally block and os._exit(0) [0 means status code]
# exit(0) means normal termination
# exit(non-zero) means abnormal termination
# If we put non-zero in this program result won't be changed

# there is only one situation where finally block won't run if PVM sees os._exit(0) before finally block
# it immediately shut down executing and won't run any code 
# when os._exit(0) runs PVM explicitly shut down

import os
try:
    print('try')
    # os_exit(1000) -> output same
    os._exit(0)  # pvm shut down here won't run next any code 
except:
    print('Except')
finally:
    print('finally')