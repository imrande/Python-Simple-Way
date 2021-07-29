# write a program for the following requirement

"""
Input :=
s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'

output :=
ax1 by2 cz3 d4 e5 f g
"""

# it can be done with zip() function but problem is zip return only 3 iterations. cause s2 contains length 3

s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'
i = j = k = 0

while i < len(s1) or j < len(s2) or k < len(s3):
    # ...
    output = ''
    if i < len(s1): 
        output += s1[i]
        i += 1
    if j < len(s2):
        output += s2[j]
        j += 1
    
    if k < len(s3):
        output += s3[k]
        k += 1
    
    print(output, end=' ')

print()