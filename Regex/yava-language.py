# Yava language Identifier =====================
# 1. Allowed characters are 
	# alphabets, digits, #
# 2. first characters should be lowercase alphabet from a to k
# 3. 2nd characters should be any digit divisible by 3 [0369]
# 4. length of identifer should be atleast 2
# regex -> [a-k][0369][a-zA-Z0-9#]*

import re

pattern = '([a-k][0369][#a-zA-Z0-9]*)'
string = input('Enter identifer: ')
match = re.fullmatch(pattern, string, re.IGNORECASE)

if match:
    print('Matched')
else:
    print('Nope')
