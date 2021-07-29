# list methods 

# extend(iterable [str, set, dict, list, tuple])
l = list(range(10))
l2 = set(range(25, 50, 5))
l.extend(l2)
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 35, 40, 45, 25, 30]

# insert(index, object)
x = [10, 20, 30, 40]

# if index is greater than(+ve) list index then value will be added at the end
x.insert(100, 9999)
print(x) # [10, 20, 30, 40, 9999]

# if index is lower than(-ve) list index then value will be added at first
x.insert(-50, 5000)
print(x) # [5000, 10, 20, 30, 40, 9999]

# remove(object)
# if object is not in list then return valueError
l = list(range(45, 100, 15))
l.remove(60)
print(l) # [45, 75, 90]

# for remove value list have 3 methods
# list.remove(obj) # in place and return None
# list.pop(optional=object) # retun removed value
# list.clear() => return [] 
# del x[0]/x => destroy completely