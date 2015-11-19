def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def b(z):
    prod = a(z, z)
    print z, prod
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print c(x, y + 3, x + y)

# print compare(1, 2)
# print compare(2, 1)
# print compare(2, 2)


