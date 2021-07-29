# read multiple values from keyboard in a single line 

num1, num2 = list(map(int, input('Enter 2 numbers: ').split()))
print('The sum is', sum(num1+num2))

# read 3 float numbers from keyboard with , separation and sum the up
try:
    num1, num2, num3 = list(map(int, input('Enter 3 numbers: ').split(',')))
except ValueError as e:
    print(e)
else:
    print('The sum is', sum((num2,num3,num1)))