# comparison operator on string
# char is compared based on ASCII values

print('durga' > 'ravi') # False (d==100 and r==114)
str1 = input('Input string: ')
str2 = input('Input str2: ')

if str1 == str2: print('Both string are equal')
elif str1 < str2: print('1st string is less than 2nd')
else: print('1st string is greater than 2nd')

# membership operator on string
# it return true if value present in string else false

print('d' in 'durga') # True

# arithmetic operator on string
# str only support + , *

# str + str -> str
# int + str -> TypeError
# str * int -> repeat str n times
# str * str -> TypeError

print('str' + 'str') # strstr
print('str' * 3) # strstrstr