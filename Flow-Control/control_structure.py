# 3 types of flow-control structure
# selection statement -> if, if else, if elif else, if elif
# iterator statement -> for, while loop
# transfer statement -> break, continue, pass

brand_name = input('Favorite brand: ')

if 'KE' == brand_name.upper(): print('It is children brand')
elif brand_name.upper() == 'KO': print('It is too light')
elif brand_name == 'pepsi': print('It is for drink')
else: print('Other are not allowed brand')