# read all lines from the file
# if readline reaches end of file its retun ''
# file.readlines() => return list of strings ['...\n', '...\n']

file = open('abc.txt')
empty_string = ''
line = file.readline().strip() # => removes whitespace

while line is not empty_string:
    print(line)
    line = file.readline().strip()
    
file.close()

print('=============================')
new_file = open('cba.txt', 'w')
new_file.writelines(['987456123\n','789456123\n'])
new_file.close()
read_lines = open('cba.txt').readlines()

for line in read_lines:
    print(line.strip())
    
open('cba.txt').close()