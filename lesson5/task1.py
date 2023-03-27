a = int(input("Print A: "))
b = int(input("Print B: "))

def exp(a, b, res = a):
    if b != 1:
        res *= a
        b -= 1
        exp(a, b, res)
    else:
        print(res)

exp(a, b)
