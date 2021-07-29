# 4 types of args accept by python function

# positional arguments
def Position_Sub(a, b):
	print(b + a)

Position_Sub(100, 200) # => 300

# keyword arguments
def Keyword_Sub(a, b):
	print(b - a)

Keyword_Sub(b = 200, a = 100) # => 100

# default arguments
def Default_Sub(a=100, b=500):
	print(b - a)

Default_Sub() # => 400

# variable argument count
def Count_Sub(*args, **kwargs,):
	print(sum(args))
	print(kwargs)

Count_Sub(1,2,3,x=5,y=8) # => 
