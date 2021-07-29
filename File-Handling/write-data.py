# 2 methods are available for write data
# file.write(str)
# file.writelines(list of strings) [any iterable(must be str)]

file = open('abc.txt', 'w')
file.write('Hello World For Python') # Hello WOrld For python
# '\n' is not default for end of each line we've to do it manually'
file.write(' & Go Dev\n') # & Go Dev
file.close()

file = open('abc.txt', 'a+')
# '\n' is not default for end of each line we've to do it manually'
file.writelines(('DurgaSoft ', 'Hello\n'))
file.writelines({'World\n': 500}) # only dict[must be str] are added
file.writelines("{'Dhaka': 1500}\n") 
d = {'100': '500'} # d.items() typeError
file.writelines(d.values())
file.close()