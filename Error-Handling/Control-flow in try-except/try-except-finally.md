```py
try:
	print('statement - 1')
	print('statement - 2')
	print('statement - 3')
except ValueError:
	print('statement - 4')
finally:
	print('statement - 5')

print('statement - 6')
```

## Case 1

If there is no exception => statement - 1, 2, 3, 5, 6 (normal termination)

## Case 2

If exception is raised at statement 2 and corresponding exception is matched => statement - 1, 4, 5, 6 (normal termination)

## Case 3

If exception is raised at statement 2 and corresponding exception isn't matched => statement - 1, 5 (abnormal termination)

## Case 4

if exception is raised at statement 4 then it is abnormal termination but before raise error finally blocked will be executed...

## Case 5

if exception is raised at statement 5/6 then it is also abnormal termination