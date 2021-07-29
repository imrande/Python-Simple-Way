# a single exception block can handle multiple exception 

def Sum_of_numbers():
    number_1 = input('Enter number ')
    number_2 = input('Enter another ')
    try:
        print(int(number_1) / int(number_2))
    except(ZeroDivisionError, ValueError) as error:
        print(f'{error.__class__.__name__}: {error}')
        
Sum_of_numbers()