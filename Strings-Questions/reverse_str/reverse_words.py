# write a python program to reverse order of words in a given string

string = input().split() # return list of string
reversed_words = string[::-1]
print(' '.join(reversed_words))

# with reversed() function
string2 = input().split()
reversed_words2 = reversed(string2)
print(' '.join(reversed_words2))