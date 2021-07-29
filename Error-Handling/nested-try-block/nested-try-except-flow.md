# Nested try-except block

```py
try:
    print('statement-1')
    print('statement-2')
    print('statement-3')
    try:
        print('statement-4')
        print('statement-5')
        print('statement-6')
    except ValueError:
        print('statement-7')
    finally:
        print('statement-8')
    print('statement-9')
except TypeError:
    print('statement-10')
finally:
    print('statement-11')

print('statement-12')
```

### Case 1

If there is no errors what is output?
- 1, 2, 3, 4, 5, 6, 8, 9, 11, 12 & normal termination.

### Case 2

If an exception is raised at statement-2 and corresponding except block matched.
- 1, 10, 11, 12 & normal termination

### Case 3

If an exception is raised at statement-2 and corresponding except block not matched.
- 1, 11 & abnormal termination.

### Case 4

If an exception is raised at statement-5 and inner except block matched
- 1, 2, 3, 4, 7, 8, 9, 11, 12 & normal termination

### Case 5

If an exception raised at statement-5 and inner except block not matched but outer matched.
- 1, 2, 3, 4, 8, 10, 11, 12 & normal termination.

### Case 6

If an exception raised at statement-5 and inner except block not matched and outer also.
- 1 ,2, 3, 4, 8, 11 & abnormal termination

### Case 7

If an exception is raised at statement 7 and outer block is matcched
- 1, 2, 3, (4,5,6), 8, 10, 11, 12 & normal termination

### Case 8

If an exception is raised at statement 7 and outer block isn't matcched
- 1, 2, 3, (4,5,6), 8, 11 & abnormal termination

### Case 9

If an exception is raised at statement 8 and outer block is matcched
- 1, 2, 3, (4,5,6,7), 10, 11, 12 & normal termination

## Case 10

If an exception is raised at statement 8 and outer block isn't matcched
- 1, 2, 3, (4,5,6,7), 11 & abnormal termination

### Case 11

If an exception is raised at statement 11 / 12  then it is abnormal termination

## Case 12

If an exception is raised at statement 10 then it is abnormal termination before throw error finally block will be executed...

## Case 13

If an exception is raised at statement 9 and outer block is matcched
- 1, 2, 3, (4,5,6,7),8, 10, 11, 12 & normal termination

## Case 14

If an exception is raised at statement 9 and outer block isn't matcched
- 1, 2, 3, (4,5,6,7), 8, 11 & abnormal termination

