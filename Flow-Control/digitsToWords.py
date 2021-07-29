# write an application to take a single number from keyboard [0 to 9] and print the number word

# 0 -> zero, 8 -> eight

number = int(input('Enter number [0-9]: '))

# 1st way
numberWords = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

print(numberWords.get(number,'out of range'))

# 2nd way
number = int(input('Enter number [0-9]: '))
numberWords_2 = ['zero','one','two','three','four','five','six','seven','eight', 'nine']

try:
    print(numberWords_2[number])
except IndexError as e:
    print(e)