# operate huge number better use generator for memory performance

import time
from random import choice

names = ['Sunny', 'Bunny', 'Chinny']
languages = ['Python', 'Java', 'C#']

print('List version'.center(25,'-'))
def people_list(number):
    return [{'id': i, 'name': choice(
            names), 'language': choice(languages)} for i in range(number)]

print(people_list(5))
t1 = time.time()
people = people_list(100000)
t2 = time.time()
print(f'Time taken for list {t2-t1}')

print('Generator version'.center(25,'-'))
def people_list(number):
    person = ({'id': i, 'name': choice(
        names), 'language': choice(languages)} for  i in range(number))
    yield person

print(people_list(5))
t1 = time.time()
people = people_list(100000)
t2 = time.time()
print(f'Time taken for gen {t2-t1}')  # it taken less time then list
