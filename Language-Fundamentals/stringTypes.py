# string is a sequence of characters
import string

string_ = 'class by \'durga\' for \"python\" very good'
string_ = """class by 'durga' for "python" very good"""
print(string_) # class by 'durga' for "python" very good

characters = string.ascii_lowercase
print(characters[3:7])
print(characters[5:1]) # ''
print(characters[20:10000]) # only remain characters

s = 'durga'
print(s.capitalize()) # Durga

s = 'durga'
print(s[0:-1]+s[-1].upper()) # durgA
