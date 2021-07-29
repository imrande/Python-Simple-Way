# filter even odd
filteredEven = filter(lambda x: (x%2) == 0, range(11))
filteredOdd = filter(lambda x: (x%2) != 0, range(11))
print(list(filteredEven))
print(tuple(filteredOdd))

# number which is divisble by 3 and odd
filtered = tuple(filter(lambda x: (x % 3 == 0 and x % 2 != 0), range(11)))
print(filtered)