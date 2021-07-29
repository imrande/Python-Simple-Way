# every python files acts as a module.

# from math1 import *
# from math2 import *
# print(sqrt(16)) [assume that sqrt is available both module. from which it's gonna run]
# python only remember the recent operation, so sqrt() will execute from math2

import dmath

print(dmath.add(10, 20)) # 30
print(dmath.product(10, 20)) # 200

# how to import module in a file
# import math
# from math import *
# from math import sqrt, pow
# from math import sqrt as square_root
# import math as math_operation