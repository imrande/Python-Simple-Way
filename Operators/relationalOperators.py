# Relational Operators >,<,<=,>=

a = 10
b = 2
print(a == b) # False
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False

# Relational operators on str ====
s1 = 'a' # ASCII value is 97
s2 = 'b' # ASCII value is 98
print(s1 == s2) # False
print(s1 > s2) # False
print(s1 < s2) # True
print(s1 >= s2) # False
print(s1 <= s2) # True

s1 = 'durga' # d = 100
s2 = 'bunny' # b = 98
print(s1 == s2) # False
print(s1 > s2) # True
print(s1 < s2) # False
print(s1 >= s2) # True
print(s1 <= s2) # False

s1 = 'durga'
s2 = 'durga'
print(s1 == s2) # True
print(s1 > s2) # False
print(s1 < s2) # False
print(s1 >= s2) # True
print(s1 <= s2) # True

s1 = [4, 5, 8] # 5 
s2 = [4, 7, 8] # 8
print(s1 == s2) # False
print(s1 > s2) # False
print(s1 < s2) # True
print(s1 >= s2) # False
print(s1 <= s2) # True

# Chaining of relational operators is possible. In the chaining, if all comparisons
# returns True then only result is True. If at least one comparison returns False then the result is False
print(10 < 20) # True
print(10 < 20 < 30) # 10 < 20 then 20 < 30 both True so  -> True
print(10 < 20 < 30 < 40) # 10 < 20, 20 < 30, 30 < 40 all are True so -> True
# 10 < 20, 20 < 30, 30 < 40, 40 > 50=False | one comparison is false so -> False
print(10 < 20 < 30 < 40 > 50)