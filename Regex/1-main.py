# Regular Expression ==> Reprsent a group of strings according to particular pattern

# Application areas of Regular Expression ==>
# 1) Validations
# 2) Pattern matching
# 3) Translators like compilers, assembler, interpreters
# 4) Develop digital circuits
# 5) communication protocols TCP/IP

# re module contains some methods :-
# 1) compile() => compile a Pattern into RegexObject
# 2) finditer() => return an iterator object which yields Match object for every Match

import re
pattern = re.compile('Python')
print(type(pattern))  # re.pattern

match = pattern.finditer('Learning Python is very easy')
print(match) # <callable_iterator object at 0x01B32D30>

# we can now call 3 methods
# start() -> return start index
# end() -> return end+1 index
# group() -> return full match object

for m in match:
    print(m.group()) # Python

# ==================================
string = "abaababa"
pattern = "ab"
match = re.finditer(pattern, string)

count = 0
for x in match:
    count += 1
    print(f'Start at {x.start()} and end at {x.end()-1} | {x.group()}')
    
print(f'Total occurrence is {count} time') # 3 times (0, 3, 5)
