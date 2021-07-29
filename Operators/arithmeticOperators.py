a, b = 10, 2

print(a + b) # 12
print(a - b) # 8
print(a * b) # 20
print(a / b) # 5.0 [this will always return float value no mater args is float or int]
print(a // b) # 5
print(a % b) # 0
print(a ** b) # 100

# '//' -> floor division operator work on both int and float values, if both value is int result must be 
# int and at least one / both values are float then result will be floating point number
print(10 // 3) # 3
print(10.5 // 3.5) # 3.0

# Assignment
print(20 / 2) # 10.0
print(20.5 / 2) # 10.25
print(20 // 2) # 10
print(20.5 // 2) # 10.0
print(30 // 2) # 15

# print('durga' + 10) TypeError: must be str(10) not int
print('durga' + str(10)) # durga10

# Arithmetic Operations on str =====
# print('durga' + 10) TypeError
print('durga' + 'Software') # durgaSoftware [concatenation]
# print('durga' - 10) TypeError
# print('durga' * 'software') TypeError
print('durga' * 2) # durgadurga
# print('durga' / 2) TypeError
# print('durga' / '2') TypeError
# print('durga' // 2) TypeError
# print('durga' % '2') TypeError

print('durga' > '2') # True
print('durga' == 2) # False
print('durga' == '2') # False
# print('durga' > 2) TypeError

# ZeroDivisionError
print(10 / 0)
print(10.0 / 0)
print(10 // 0)
print(10.0 // 0)
print(10 % 0)

# internally True == 1 and False == 0 so any operation is possible
print('imran' * True) # imran
print('imran' * False) # nothing
# print('imran' + True) TypeError
# print('imran' + False) TypeError