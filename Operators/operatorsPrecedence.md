# Python Operators Precedence

```py
print(10 + 2 * 3) # 16
print((10 + 2) * 3) # 36
```

## Highest to lowest

- ( )
- **
- ~, ~-
- /, *, //, %
- +, -
- <<, >>
- &
- ^
- |
- <, >, <=, >=, ==, !=
- +=, -=, *=, /=, //=
- is, is not
- not in, not
- not
- and
- or

```py
a, b, c, d = 30, 20, 10, 5
print((a+b) * c/d) # 100.0
print((a+b) * (c/d)) # 100.0
print(a + (b*c)/d) # 70.0
```
