# range is represents a sequence of number, it is immutable

r = range(10) # 0 ... 9
print(r) # range(0, 10)
print(type(r)) # range

for i in range(5):
    print(i, end='|') # 0|1|2|3|4
print()

r = range(20, 5, -5) # for -ve step BEGIN value must be > than END value else IndexError: out of range
rr = range(5, 20, 5) # range(5, 20, 5) for +ve step END value must be > than BEGIN value else IndexError: out of range
print(rr[0:2]) # range(5, 15, 5) (up to 15)
print(r[0:2]) # range(20, 10, -5) [10 is ending point & it's not included]
print(r[0]) # 20
print(r[1]) # 15
