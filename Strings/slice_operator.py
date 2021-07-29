# str[start:end:step]
# if step is +ve then forward direction (left to right)
# if step is -ve then backward direction (right to left)
# start value forward direction is always 0
# start value for backward is always -1

string = 'abcdefghij'

print(string[1:6:2]) # bdf
print(string[::1]) # abcdefghij
print(string[0::1]) # abcdefghij
print(string[::-1]) # jihgfedcba
print(string[-1::-1]) # jihgfedcba
print(string[3:7:-1]) # ''
print(string[-3:-7:-1]) # hgfe
print(string[7:4:-1]) # hgf
print(string[0:10000:1]) # abcdefghij
print(string[4:1:-1]) # edc
print(string[4:1:-2]) # ec
print(string[-4:1:-1]) # gfedc
print(string[-4:1:-2]) # gec
print(string[5:0:1]) # '' [end point is 0]
# print(string[9:0:0]) ValueError: step can't be 0
print(string[10000:2:-1]) # jihgfed
print(string[10:-1:-1]) # '' [end point is -1]
print(string[5:9:-2]) # ''
print(string[-5:9:-2]) # ''
print(string[0:-9:-2]) # ''
print(string[0:0:1]) # ''
print(string[0:-11:-1]) # a (0 to -11, in the middle -10 is there so a)
print(string[0:-10:-1]) # ''
print(string[5:5:2]) # ''