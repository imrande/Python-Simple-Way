# we can access list values by
# index
# slice operator

# by index
l = list(range(11))
print(l[0]) # 0
print(l[-1]) # 10

# by slice operator
# +ve[step] => forward direction (begin to end-1)
# -ve[step] => backward direction (begin to end+1)

list_values = list(range(10, 110, 10))
print(list_values[2:7]) # [30, 40, 50, 60, 70]
print(list_values[2:7:2]) # [30, 50, 70]
print(list_values[4::2]) # [50, 70, 90]
print(list_values[8:2:-2]) # [90, 70, 50]
print(list_values[4:100]) # [50, 60, 70, 80, 90, 100]
print(list_values[4:0:2]) # []