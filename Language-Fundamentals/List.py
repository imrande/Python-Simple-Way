# If we want to represent a collection of values in a single entity, where duplicates are allowed and order is
# preserved then we can use list

# characteristic's of list:=
# 1) order is preserved
# 2) duplicates are allowed
# 3) list is represented by []
# 4) list is mutable
# 5) growable in native [in place]
# 6) support heterogeneous(different type) objects
# 7) positive and negative indexing are possible

l = list()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l) # [10, 20, 30, 40]
l.remove(30)
print(l) # [10, 20, 40]

print(__doc__) # None 
