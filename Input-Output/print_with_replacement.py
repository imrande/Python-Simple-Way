# print something with replacement operator

name = 'durga'
salary = 10000
girlfriend = 'X'

# followed by positional arguments
print('Hello {}, your salary is {} and your friend {} is waiting at the new market'.format(name, salary, girlfriend)) 

 # order can be changeable
print('Hello {2}, your salary is {1} and your friend {0} is waiting at the new market'.format(name, salary, girlfriend))

print('Hello {n}, your salary is {s} and your friend {gf} is waiting at the new market'.format(n=name, s=salary, gf=girlfriend))
