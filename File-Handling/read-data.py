# there are 4 ways we can read data 

# file.read() => read total data character by character
# file.read(n) => read only n character
# file.readline() => read only one line each time
# file.readlines() => read all lines and return each line as list item
# file.readlines(n) => read n chars and return list item **

file = open('abc.txt')
print(file.read()) # => read all chars
print('====')
file.seek(0)
# print(file.read(n)) => if n is beyond the len(file) or -ve value we'll get full data
print(file.read(12)) # => Hello World
file.close()