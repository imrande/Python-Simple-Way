# if we want to automatically close the file after completing task, 
# best is open file with statement
  
with open('cba.txt') as file:
	print(file.readline().strip())
	print(file.closed) # False

print(file.mode) # 'r'
print(file.closed) # True

"""==============Q&A===============
what's difference between:-
1) f = open('anc.txt', 'w') and
2) with open('abc.txt', 'w') as file:

1. in this case we've to close the file explicitly
2. in this case we don't need to close the file explicitly, with statement handle it...
"""
