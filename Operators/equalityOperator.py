# Equality Operator ==, !=

a, b = 10, 20
print(a == b) # False
print(a != b) # True

# Chaining concept is applicable for equality operators. If at least one comparison
# returns False then the result is False. Otherwise the result is True
print(10 == 20 == 30==40) # False
print(10 == 10 == 10 == 10) # True

# What's difference between '==' and 'is' operator?
# == operator is for value comparison
# is operator is for reference obj/address comparison
