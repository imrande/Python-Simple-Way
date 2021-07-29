# Generator is a special type of functions which is generate sequence of values 
# it's forget past value only remember current value and near future value
# Advantage of Generator :-
	# 1) performance improvement
	# 2) memory utilization improvement
	# 3) compare with iterators(list, tuple, dict), generators(range, zip) are easy to use
	# 4) best suitable for web scraping, playing with big data
# Limitation :-
	# isn't store data
	# so any get particular index value not possible

from time import sleep

# write a generator function to generate 3 values 'A', 'B', 'C'
def my_generator():
	yield 'A'
	yield 'B'
	yield 'C'

print(type(my_generator()))
result_generator = my_generator()
print(next(result_generator))
print(next(result_generator))
print(next(result_generator))

# print nothing cause it remebers just current value and upcoming values
# that's why after one iteration next iteration is not possible
print(my_generator())
for i in result_generator:
	print(i)

# write a generator function to generate first n values
def generate_n(n):
	i = 1
	while i <= n:
		yield i
		i += 1

sequence_of_values = generate_n(5)
for  i in sequence_of_values: 
	print(i)

print('-'*20)
# write a generator function to generate values for countdown with provided max value
def generate_countdown(maxValue):
	while maxValue >= 1:
		yield maxValue
		maxValue -= 1

countdown = generate_countdown(10)
print(next(countdown))

for i in countdown:
	print(i)
	sleep(1)