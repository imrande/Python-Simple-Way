# Split of string

s = 'Durga software solutions'.split()
print(s)

date = '05-04-2019'.split() # ['05-04-2019']
date = '05-04-2019'.split('-')
print(date)
print(':'.join(date))

new_date = [15,10,2019]
print('-'.join((str(x) for x in new_date)))
