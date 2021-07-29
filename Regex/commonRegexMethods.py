import re

# match() -> check the given pattern at beginning of the target string 
# if then returns match obj else None
match = re.match('ab', 'abbaadg')
print(match) # -> <re.Match object; span=(0, 2), match='ab'>

# fullmatch(pattern, targetStr) -> Regex has to be full matched with Target str
match = re.fullmatch('ab', 'abbaadg') # None
match = re.fullmatch('abc', 'abc') 
print(match) # <re.Match object; span=(0, 3), match='abc'>

# sub() -> replacementStr
# re.sub(regex, replacementStr, targetString)
# return -> resultStr
s = re.sub('\d', '@', '789efr')
print(s)  # -> @@@efr

# subn() -> how many replacement is happended 
# re.subn(regex, replacementStr, targetString)
# return -> tuple(resultString, number of replacement)
s = re.subn('\d', '_', '789efr')
print(s)  # -> ('___efr', 3)

# split() -> same as method in string, return a list according to matchstring from  a string
splitSite = re.split(r'\.', 'www.google.com')
print(splitSite) # -> ['www', 'google', 'com']

# findall(regex, str) -> return list of str all matched object
findAll = re.findall('\d', 'a7b9k6z')
print(findAll)  # ['7', '9', '6']

# search() -> match object of the first occurence inside the str else None
match2 = re.search('ba', 'abbacdbag')
print(match2)  # <re.Match object; span=(2, 4), match='ba'>

if match2:
    print(match2.start(), "...", match2.end()) # 2 ... 4

# finditer() -> return regex obj
mm = re.finditer('\d', 'a7bk9z6')
for m in mm:
    print(m.group()) # -> 7 -> 9 -> 6

# ============================================
# serach(pattern, string, re.IGNORECASE)
# if I want to ignore case sensitive problem
# by default not match until i use IGNORECASE attribute
searching = re.search('^easy', 'EAsY is always easy', re.IGNORECASE)
if searching:
    print('Matched') # Matched
else:
    print('Not Matched')
