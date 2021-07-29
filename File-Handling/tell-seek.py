# we can use tell() method to return current position of the cursor from the beginning
# we can use seek() method to move cursor to specified locarion...

with open('file.txt', 'w') as f:
	f.writelines([
		'Durga\n',
		'Software\n',
		'Solutions\n'
		'Hyderabad\n'
	])

with open('file.txt') as file_read:
	print(file_read.tell()) # 0
	print(file_read.read(2)) # Du
	print(file_read.tell()) # 2
	print(file_read.read(4)) # rga\n
	print(file_read.tell()) # 7 ?
	print(file_read.readline().strip()) # SOftware
	print(file_read.tell()) # 17 ?
	print(file_read.read(3)) # Sol
	print(file_read.tell()) # 20
	print(file_read.seek(25)) # 25
	print(file_read.tell()) # 25

