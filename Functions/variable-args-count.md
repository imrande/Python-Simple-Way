# Important Conclusion about `**, *`

- Main difference between `*args` and `**kwargs`
- args is variable length arguments and return ()
- `**kwargs` is variable keyword arguments and return {}

after variable length args if we take any args we've to call them explicitly as keyword args otherwise SyntaxError

```py
# def f1(x, *y): => valid  (1st value would be x)

def f1(*x, y):
	print(x)
	print(y)

f1(10, 20, 30, y=40)

```

```py
# we can't take more than one variable args count

def f2(*x, *y): # => Error
	print(x)
	print(y)

f2(10, 20, 30, 40)

```

```py
# SyntaxError
def f3(**x, y):
	print(x)
	print(y)

```

```py
# SyntaxError
def f3(**x, **y):
	print(x)
	print(y)

```

```py
# SyntaxError
# def f1(*x, **y): => valid

# after keyword args we can't take positional
def f1(**x, *y):
	print(x)
	print(y)

```