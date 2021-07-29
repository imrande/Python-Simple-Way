# example for best practice else block

file = None
try:
    file = open('abc.txt', 'r')
except FileNotFoundError as e:
    print(e.__class__.__name__, e)
else:
    print('File Opened Successfully')
    print("The content of the file is")
    print(file.read())
finally:
    if file is not None:
        file.close()