# Check bd mobile number is valid or not

import re

mobileNumberInput = input("Enter mobile number: ")
# mobileNumberInput = '017xxxxxxxx'
regexPattern = '01[3-9][0-9]{8}'

pattern = re.fullmatch(regexPattern, mobileNumberInput)

print(pattern.group() if pattern else "Nope")

