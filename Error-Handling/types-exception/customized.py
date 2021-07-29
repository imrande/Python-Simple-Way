class TooYoungError(Exception):
    def __init__(self, message):
        self.message = message

class TooOldError(Exception):
    def __init__(self, message):
        self.message = message

age = int(input("Enter age: "))
if age > 60:
    raise TooYoungError('Please wait some more time, we are trying our best')
elif age < 18:
    raise TooOldError('Please make sure you are old enough for marriage')
else:
    print('Thanks for registration! you get mail soon')
