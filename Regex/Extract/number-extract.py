# extract number from input file

import re
inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

for line in inputFile:
   mobileNumber = re.findall('[6-9][0-9]{10}', line)

    for number in mobileNumber:
        outputFile.write(number + '\n')

outputFile.close()
inputFile.close()
