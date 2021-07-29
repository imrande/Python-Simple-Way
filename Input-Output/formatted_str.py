# print with formatted string

# %d / %i == number
# %s == str, list, tuple, dict
# %f == float
a = 10
print('a is %i' %a)

a, b, c = 10, 20.5, '30'
print('a is %d, b is %f, c is %s' % (a, b, c))

name = 'Durga'
marks = tuple(range(10, 50, 10))
print("Hello %s, your marks are %s" % (name,marks)) # Hello Durga, your marks are (10, 20, 30, 40)

# price casting
price = 70.56784
print('Price value is {:0.2f}'.format(price)) # 70.57
print("Price value is %.2f" %price) # 70.57
