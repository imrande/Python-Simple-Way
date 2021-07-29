# If we want to represent a collection of values in a single entity, 
# where duplicates are not allowed and order is not required then we can use set

# characteristic's of set:=
# 1) order is not preserved
# 2) duplicates are not allowed
# 3) set is represented by set() / {}
# 4) set is mutable
# 5) growable in native [in place]
# 6) support heterogeneous (different types) objects
# 7) indexing and slicing is not possible

s = {10, 20, 30}
print(type(s)) # set
s = {10, 20, 10, 'durga', 30, 40}
print(s) # {10, 20, 30, 40, 'durga'}

# empty set
s = set()
s = {} # dict

new_set = {10, 20, 30, 40}
new_set.add(50) # in place
print(new_set) # {10, 20, 40, 50, 30}
new_set.remove(30) 
print(new_set) # {10, 20, 40, 50}

# ================================= frozenset() =======================================
# frozenset is immutable unordered collection of unique elements
s = {10, 20, 20}
frozenSet = frozenset(s)
print(frozenSet) # {10, 20}
print(type(frozenSet)) # frozenset
