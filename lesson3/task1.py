N = int(input("Enter number of elements in the list: "))
elements = input("Enter list of elements separated by space: ").split(' ')
X = str(input("Enter number to search: "))

if len(elements) != N:
    print("Number of elements in the list doesn't match N")
else:
    print(f"Found X {str(elements.count(X))} times")
