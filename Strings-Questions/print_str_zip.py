s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'

x = zip(s1, s2, s3)

for w in x:
    print(''.join(w), end=' ')
print()