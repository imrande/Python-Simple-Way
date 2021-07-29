# ============================== int() ==========================
print(int(True)) # 1
print(int(False)) # 0
print(int(.5)) # 0
# print(int('g')) -> ValueError: Invalid literal for int() with base=10
# print(int('10.0')) -> ValueError: Invalid literal for int() with base=10
print(int(0xFace)) # 64206
print(int(0o123)) # 83
print(int(0b1111)) # 15
# print(int(2+5j)) -> TypeError: Can't convert complex to int
print(int('10')) # 10
# print(int('10.89')) -> ValueError: Invalid literal for int() with base=10

# ============================== float() ==========================
# we can represent float value only decimal form which is base 10. Other forms (octal, binary, hexa) are not allowed
f = 125.5
# f = 0b11.1 -> SyntaxError
# f = 0o45.2 -> SyntaxError
# f = 0xFa3.5 -> SyntaxError
print(float(10)) # 10.0
print(float(0b1111)) # 15.0
print(float(0o456)) # 302.0
print(float(False)) # 0.0
print(float(True)) # 1.0
print(float(0xFace)) # 64206.0
print(float('10')) # 10.0
print(float(100.5)) # 100.5
print(float('100.0')) # 100.0
# print(float(20+5j)) TypeError: Can't convert complex to float

# ============================== complex() ==========================
# j^2 is -1 so j is √-1
print(complex(200)) # 20+0j
print(complex(20.5)) # 20.5+0j
print(complex(0b1111)) # 15+0j
print(complex(True)) # 1+0j
print(complex(0xFace, 0b1111)) # (64206+15j)
print(complex('10')) # (10+0j)
print(complex('10.5')) # 10.5+0j

print(complex(10, 20)) # 10+20j
print(complex(25.5, 45)) # 20.5+45j
# print(complex('10', '20')) TypeError: complex() can't take second arg if first is a string
# print(complex('10', 20)) TypeError: complex() can't take second arg if first is a string
# print(complex(10, '50')) TypeError: complex() second arg can't be a string

# ============================== bool() ==========================
print(bool('')) # False
print(bool(12)) # True
print(bool(2+8j)) # True
print(bool(0+0j)) # False
print(bool(1+0j)) # True
print(bool(0xFade)) # True
print(bool('string')) # True
print(bool(0.1)) # True
print(bool(0.0)) # False
print(bool('False')) # True

# ============================== str() ==========================
print(str(0b1111)) # '15'
print(str(115)) # '115'
print(str(0.5)) # '0.5'
print(str(5+2j)) # '5+2j'
print(str(True)) # 'True'
