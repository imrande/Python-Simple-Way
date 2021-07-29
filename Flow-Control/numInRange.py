# write an application to check wheather the number in the given range(0, 100) or not

n = int(input('Enter number: '))

# 1st way
if 0<=n<=100: print(f'{n} is in range')
else: print(f'{n} is not in range')

# 2nd way
if n in range(0, 101): print(f'{n} is in range')
else: print(f'{n} is not in range')
