# to check type of character present in string

# isupper(), isalpha(), islower(), isalnum(), istitle(), isspace(), isdigit()

print('ABC458'.isupper()) # True => it just check string contains uppercase letters or not, doesn't care about digit
print('ABCo458'.isupper()) # False => It contains lowercase
print('abc458'.islower()) # True
print('abcA78'.isupper()) # False 
print('789abc'.isdigit()) # False
print('789abc'.isalpha()) # False
print('abc'.isalpha()) # True
print('789'.isdigit()) # True
