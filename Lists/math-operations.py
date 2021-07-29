# concatenate operator(+)
l = list(range(5))
k = list(range(6,11))
# O(n) time complexity
# can only concate list+list [not other types else TypeError]
print(l+k) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# repetition operator(*)
# work with only str, list and tuple, TypeError occurred for set & dict
# (iterable * int) => without int float is typeError

l = [4]
print(l * 2) # [4, 4]

l = (5,)
print(l*3) # (5,5,5)
