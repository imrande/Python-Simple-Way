# Generate square of numbers
mappingNumber = list(map(lambda x: x*x, range(5)))
print(mappingNumber)

# map with multiple iterations
mapping = list(map(lambda x, y, z: x+z+y, range(5), range(6, 11), range(12, 18)))
print(mapping) # => [18, 21, 24, 27, 30]