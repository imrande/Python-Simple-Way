# write a program to find biggest in a 3 number

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

if b < a > c: print(f'{a} is biggest')
elif b < c: print(f'{c} is biggest')
else: print(f'{b} is biggest')