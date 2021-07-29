# If we want to represent a collection of values in a single entity, where duplicates are allowed and order is
# preserved and values are immutable/read only then we can use tuple

# characteristic's of tuple:=
# 1) order is preserved
# 2) duplicates are allowed
# 3) tuple is represented by ()
# 4) tuple is immutable
# 6) support heterogeneous(different type) objects
# 7) positive and negative indexing are possible

l = tuple((10, 20, 30, 40))
print(l) # (10, 20, 30, 40)
print(l[-1]) # 40
print(l[2:]) # (30,40)

x = (10) # int type
x = (10,) # tuple type
print(type(x)) # tuple
