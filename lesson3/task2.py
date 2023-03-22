N = int(input("Enter number of elements in the list: "))
elements = list(map(int, input("Enter list of elements separated by space: ").split(' ')))
X = int(input("Enter number to compare: "))

if len(elements) != N:
    print("Number of elements in the list doesn't match N")
else:
    res = elements[0]
    for i in range(1, N):
        if (abs(res - X) > abs(elements[i] - X)):
            res = elements[i]
    print(f"the closest number is {res}")
