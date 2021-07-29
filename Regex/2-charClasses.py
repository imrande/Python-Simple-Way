import re

# Character Classes ===========
# [abc] Either a OR b OR c
# [^abc] Except a and b and c
# [a-z] Any Lower case alphabet symbol
# [A-Z] Any upper case alphabet symbol
# [a-zA-Z] Any alphabet symbol either upper or lower
# [0-9] Any digit from 0 to 9
# [a-zA-Z0-9] Any alphanumeric character
# [^a-zA-Z0-9] Except alphanumeric characters(Special Characters)

match = re.finditer('[a-z]', 'a789@bk9z')
for m in match:
    print(m.group()) # a | b | k | z

# Pre-defined char classes ============
# \s ==> space character
# \S ==> except space character
# \W ==> except alpha numeric character only spacial character | [^a-zA-Z0-9]
# \w ==> any alpha numeric char | [a-zA-Z0-9]
# . ==> any character
# \d ==> any digit | [0-9]
# \D ==> except any digit (alphabet + special chars)

matchPattern = re.finditer(r'\w', 'a7b @k9z')
for match in matchPattern:
    print(match.group()) # a | 7 | b | k | 9 | z
