from sys import argv

print('The number of cmd line args', len(argv)) # be default len is 1(file_name)
print(type(argv)) # list
print('The list of cmd line args', argv) # ['...']
print('Print all values')
argv.remove(argv[0]) # it removes first index value which is file_name

for i in argv: 
    print(i)

# program to print sum of given numbers provided as cmd line args
print('The sum is ', 0) if argv == [] else print('The sum is', sum((int(i) for i in argv)))

# space is the separator between command line args. All args are str by default
# long space separator string should be enclosed by "" (python file.py "Leya Falcon") otherwise it will consider each as different string
# if we put '', it will return (argv[1]) only 'file_' (python file.py 'file_ x.txt') [ takes space as separatoor]

# print(argv[100]) => try to print out of range, it will return Indexerror: out of range
