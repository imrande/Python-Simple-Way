# write an application to take a single number from keyboard [0 to 99] and print the number in word

words_to_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six','seven','eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen','seventeen','eighteen', 'nineteen']

words_20_to_100 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

number = int(input('Number: '))

try:
    if number == 0: print('zero')
    elif number < 20: print(words_to_19[number])
    elif number >= 20: print(words_20_to_100[number // 10]+' ' +words_to_19[number % 10])
except IndexError as e:
    print(e)