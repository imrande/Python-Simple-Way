# generate fibonaci number using generator 0,1,1,2,3,5...

def fibo_number():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, b + a

for i in fibo_number():
    if i > 100:
        break
    print(i)
