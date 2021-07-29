s = 'ABCDEFGHE'

# find(substr, start, end)
print(s.find('E')) # 4
print(s.find('e')) # -1 (not found so return -1)

# rfind(substr, start, end)
print(s.rfind('E')) # 8 [start searching from backward but return +ve index only]
print(s.rfind('Z')) # -1

# index() [if substr is not available return valueError]
print(s.index('B')) # 1
# print(s.index('Z')) valueError

# rindex() [if substr is not available return valueError]
print(s.rindex('E')) # 8
# print(s.rindex('W')) valueError

# difference between find and index is find return -1 if substr is not available where index return ValueError