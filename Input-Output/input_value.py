# in python 2.x
# return type of raw_input() is str
# return type of input() is based on value

# in python 3.x
# return type of input() is str

# sum of 2 numbers
x = int(input('Enter number: '))
y = int(input('Enter number2: '))
print('Sum is', sum((x,y)))

# one linears
numbers = [int(i) for i in input('Enter 2 numbers: ').split()]
print('Sum is', sum(numbers))

# write a program to read employee data from keyboard and print the data
employee = {
    'compnay_name': input('Company: '),
    'name': input('Name: '),
    'id': int(input('ID: ')),
    'salary': float(input('Salary: ')),
    'address': input('Address: '),
    'married': eval(input('married_status[True|False]: '))
}

print(employee)

# in string to boolean conversion where answer is true or false from user, eval() is best suit for it
# bool('False') => True [require False]
# eval('False') => False