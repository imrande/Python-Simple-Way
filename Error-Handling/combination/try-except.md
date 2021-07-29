# Perfect combination of try-except-else-finally block

## combination 01

```py
try:
  print('try')
# Syntax error [except or finally must be required]
```

## combination 02

```py
except:
  print('except')
# Syntax error [try must be required]
```

## combination 03

```py
else:
  print('else')
# Syntax error [try and except must be required]
```

## combination 04

```py
finally:
  print('finally')
# Syntax error [try is required]
```

## combination 05

```py
try:
  print('try')
except:
  print('except')
# valid combination
```

## combination 06

```py
try:
  print('try')
else:
  print('else')
# syntax error [except is required before the else block]
```

## combination 07

```py
try:
  print('try')
finally:
  print('finally')
# valid combination
```

## combination 08

```py
try:
  print('try')
else:
  print('else')
except:
  print('except')
# syntax error [except must be before else block]
```

## combination 09

```py
try:
  print('try')
else:
  print('else')
finally:
  print('finally')
# syntax error [except must be before else block]
```

## combination 10

```py
try:
  print('try')
except:
  print('except')
else:
  pass
finally:
  pass
# valid syntax
```

## combination 11

```py
try:
  pass
except:
  pass
try:
  pass
finally:
  pass
# valid syntax
```

## combination 12

```py
try:
  pass
except:
  pass
try:
  pass
else:
  pass
# invalid [syntax error except is required before else]
```

## combination 13

```py
try:
  pass
except ZeroDivisionError:
  pass
except ValueError:
  pass
# valid syntax
```

## combination 14

```py
try:
  pass
except:
  pass
else:
  pass
else:
  pass
# syntax error
```

## combination 15

```py
try:
  print('try')
except:
  print('except')
finally:
  pass
finally:
  pass
# syntax error [only 1 finally block is required]
```

## combination 16

```py
try:
  pass
except:
  pass
if 10 < 20:
  print('if')
else:
  print('else')
# valid syntax
```

## combination 17

```py
try:
  print('hello')
print('Hello, World')
except:
  print('except')
# syntax error
```

## Combination 18

```py
try:
  print('try')
except:
  print('except')
print('Hello')
except:
  print('except')
# Invalid synatx
```

## Combination 19

```py
try:
  print('try')
except:
  print('except')
print('Hello')
else:
  print('else')
# Invalid synatx
```

## Combination 20

```py
try:
  print('try')
except:
  print('except')
print('Hello')
finally:
  print('finally')
# Invalid synatx
```

## Combination 21

```py
try:
  try:
    print('Inner try')
  except:
    print('Inner except')
  finally: print('Inner finally')
except: print('Outer except')
# Valid Syntax
```

## Combination 22

```py
try:
  print('try')
except:
  try:
    print('inner try')
  except: print('inner except')
# valid syntax
```

# Combination 23

```py
try:
  print('try')
except:
  print('except')
else:
  try: pass
  except: pass
# Valid syntax
```
# Combination 24

```py
try:
  print('try')
except:
  print('except')
finally:
  try: pass
  except: pass
# Valid syntax
```
# combination 25

```py
try:
  try: print('inner try')
except:
  print('except')
# Invalid syntax
```

## COmbination 26

```py
try:
  try: print('try')
  finally: print('finally')
except: print('except')
```
