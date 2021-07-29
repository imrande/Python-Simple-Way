# bytes data types are useful when deal with binary data [images, files]
# bytes value range is range(0, 256) [up to & not including], more than 255 is ValueError
# immutable
# iterable

l = list(range(10, 50, 10))
b = bytes(l)
print(b) # b'\n\x14\x1e('
print(type(b)) # bytes
print(b[0]) # 10
print(b[2:]) # b'\x1e('

# >>> [x for x in b] => [10, 20, 30, 40]

# ========================================== byteArray() ===============================
# byteArray value range is range(0, 256), more than 255 is ValueError
# mutable
# iterable, sliceable, indexing allowed

ll = list(range(10, 50, 10))
b = bytearray(ll)
print(type(b)) # bytearray
print(b)
print(b[-1])
print(b[2:])
b[0] = 00
# >>> [x for x in b] => [10, 20, 30, 40]
