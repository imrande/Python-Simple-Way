# regex important methods ==================
# match(pattern, str) 
    # to check given pattern at beginning of the string if it is then return match objects else None [like as ^a]
# fullmatch(pattern, str) 
    # to match full string if match then retun match obj else None []
# search() 
    # search the given pattern in given string if match return obj else return None or first occurrence (if match) [a{n}]
# findall() 
    # find all matches [abc]
# finditer()
# sub()
# subn()
# split()
# compile()

import re
match = re.finditer('ab', 'abaabaaaba')

for m in match:
    print(m.start(), '...', m.group(), '....', m.end())

# Quantifiers ========================
# We can use quantifiers to specify the number of occurrences to match.

# 'a' means exactly one 'a'
# 'a+' means at least one 'a'. It will return ['a', 'aa', 'aaa'] | at least one 'a' ('aaa' consider as a sinlge char)
# 'a*' means any number of 'a' including zero number of 'a' also | index is (0 to end+1), 'aaa' consider as a sinlge char
# 'a?' means atmost one 'a' or including zero number of 'a' | combination of (a* & a+)
    # either one 'a' or 0 number of 'a'. (it doesn't consider 'aaa' as a single rather return 'a', then 'a' , then 'a')

# 'a{n}' means exactly n number of a match (group)
    # re.finditer('a{3}','aaa7b @k9z') -> it will return where exactly 3 a (0 to 2)
# 'a{m,n}' means min of m and max of n number of a (group)

# [^a] means except a
# ^a means start with a
# a$ means end with a
