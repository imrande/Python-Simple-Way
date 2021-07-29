# check car number is valid or not

import re
carRegistrationNum = 'TS23EK7860'
rePattern = r'[A-Z]+[012][0-9][A-Z]{2}[0-9]{4}'
patternMatch = re.findall(rePattern, carRegistrationNum, re.IGNORECASE)
print(patternMatch[0] if patternMatch else "Invalid")
