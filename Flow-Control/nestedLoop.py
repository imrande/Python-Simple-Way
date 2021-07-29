# Break statement
for i in range(3): # 0 1 2
    for j in range(3): # 0 1 2
        if i == j: break
        print(i,j) # 1 0 -> 2 0 -> 2 1



# continue statement
for i in range(3): # 0 1 2
    for j in range(3): # 0 1 2
        if i == j: break
        print(i,j) # 0 1 -> 0 2 -> 1 0 -> 1 2 -> 2 0 -> 2 1

# pass statement
class Loan():
    pass

# pass statement acts as empty statement in python
# pass acts as placeholder to future code implementation
# To define an abstract method [method without a body] pass statement is best