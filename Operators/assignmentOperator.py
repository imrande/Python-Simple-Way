# assignment operators are +=, -=, *=, /=, //=, **=, |=, ^=, &=, <<=, >>=

# ++x and -x/--x has no effect in place for changing value of x
x = 5
++x
print(x) # 5
print(+++++x) # 5

y = 10
-y
print(y) # 10
print(-y) # -10

# in python, there is no such kind of operators x++ and x--, it's produce SyntaxError
a = 10
# a++ SyntaxError
print(10) # 10
# print(a++) SyntaxError

b = 20
# b-- SyntaxError
print(b) # 20
# print(b--) SyntaxError