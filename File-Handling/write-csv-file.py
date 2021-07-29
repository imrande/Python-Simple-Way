import csv

with open('emp.csv', 'w', newline='') as write_csv:
	w = csv.writer(write_csv)
	w.writerow(('ID', 'Name', 'Salary', 'Location'))

	while True:
		ID = input('Enter your id ')
		salary = float(input('Enter your salary '))
		name = input('Enter your Name ')
		loc = input('Enter your Location ')

		w.writerow({ID, name, salary, loc})

print(f'Writing on "emp.csv" file is successful')