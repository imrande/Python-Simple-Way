# Python has no ternary operator unlike javaScript, cpp
# It has statement which works like ternary

# value if else value

a, b = 10, 20
c = 30 if a > b else 40
print(c) # 40

# read 2 values from keyboard and print min value by using ternary
num_1 = int(input('Enter num1 <<< '))
num_2 = int(input('Enter num2 <<< '))

min_value = num_1 if num_1 < num_2 else num_2
print(min_value)

# read 3 values from keyboard and print min value by using ternary
num1 = int(input('Enter num1 <<< '))
num2 = int(input('Enter num2 <<< '))
num3 = int(input('Enter num3 <<< '))

# num1 < num2 and num1 < num3 == num2 > num1 < num3
min_value = num1 if num2 > num1 < num3 else num2 if num2 < num3 else num3
print(min_value)

# num1 > num2 and num1 > num3 == num2 < num1 > num3
max_value = num1 if num2 < num1 > num3 else num3 if num2 < num3 else num2
print(max_value)

# if both number is same then return 'both are equal'
# if num1 is greater than num2 return 'greater'
# if num1 is less than num2 return 'smaller'

a = int(input('<<< '))
b = int(input('<<< '))

result = 'both are equal' if a == b else 'greater' if a > b else 'smaller'
print(result)