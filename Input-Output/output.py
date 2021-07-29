# print() without args, its return newline

a, b, c = 10, 20, 30
print('Values are:', a, b, c) # Values are: 10 20 30
print('Values are:', a, b, c, sep='|') # Values are:|10|20|30

# print multiple values in a single line
print('hello', end='')
print('durga', end='')
print('soft') 
# hellodurgasoft

print('Hello', 'Rena', sep=',', end='🥰') # Hello,Rena🥰
print()

print(10, 20, 30, sep=':', end='***')
print(40, 50, 60, sep=':')
print(70, 80, sep='**', end='$$')
print(90,100) 
print(1000)
# 10:20:30***40:50:60
# 70**80$$90 100
# 1000

# difference between below code
print('durga', 'software') # two str will be printed separated by space 'durga software'
print('durga' + 'software') # str concatenation will be happended and convert it single str 'durgasoftware'
