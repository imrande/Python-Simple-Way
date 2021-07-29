# else-block with try-except finally

# Case 1
x = 10

if x > 10:
    print('x is 10')
else:
    print('x is not 10')

# Case 2
# [for-else] else block will execute if no break statement in the loop, 
# if have any break else won't be executed [same as for loop or while loop]

for i in range(0, 10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4
else:
    print('Done!')

# Case 3
for i in range(0, 10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9 Done!
else:
    print('Done!')

# Case 4
count_ = 1
number = 5
fact = 1

while (number >= count_):
    fact *= count_
    count_ += 1
else:
    print('I got factorial number')  # executed

print(fact)

# Case 5
# try-except-else-finally
# else block will be executed only if no error in try block

try:
    print(1)  # 1
except:
    print(2)
else:
    print(3)  # 2
finally:
    print(4)  # 3

# case 5
# else block won't be executed if found error in try block
try:
    print(10 / 0)
except ZeroDivisionError:
    print('Division error')  # 1
else:
    print('I am else')
finally:
    print('I am finally')  # 2

# Case 6
# except block is compulsory for else block otherwise SyntaxError
try:
    print(5)
else:
    print('Done')
finally:
    print('finally')

