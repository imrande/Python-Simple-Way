# check whether two strings are anagram or not
# if both string contains same element then it can be called anagram, order is not important

string = input()
string2 = input()

if sorted(string) == sorted(string2):
    print('They are anagram')
else:
    print('They aren\'t anagram')