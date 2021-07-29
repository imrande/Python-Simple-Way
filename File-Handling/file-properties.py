# file object has some properties and methods

file = open('abc.txt', 'w')

print('File Name', file.name) # => 'abc.txt'
print('File Mode', file.mode) # => 'w'
print('File is closed', file.closed) # => False

print('Is file readable?', file.readable()) # => False
print('Is file writeable?', file.writable()) # => True
file.close()

print('File is closed', file.closed) # => True

