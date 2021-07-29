# read data from (input.txt) file and write data to (output.txt) file

input_file = open('input.txt')
output_file = open('output.txt', 'w')
reading_data = input_file.read()
output_file.write(reading_data)

input_file.close()
output_file.close()
