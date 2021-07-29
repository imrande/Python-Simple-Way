# Read and write data on binary file
# this verison is stay forwad, better use third party library(pillow, opencv) etc

# read the binary data
with open('input.png', 'rb') as read_data:
	read_binary_data = read_data.read()
	print(type(read_binary_data)) # 'bytes'

# write data
with open('output.jpg', 'wb') as write_data:
	write_data.write(read_binary_data)

