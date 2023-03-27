a = int(input("Print A: "))
b = int(input("Print B: "))

def my_sum(a, b, res = 0):
    if a == b == 0:
        print(res)
    else:
        if a > 0:
            res += 1
            a -= 1
        if b > 0:
            res += 1
            b -= 1
        my_sum(a, b, res)

my_sum(a, b)
