my_list = list(map(int, input("Enter list: ").split()))
my_min = int(input("Enter min: "))
my_max = int(input("Enter max: "))

res = []

for i in range(len(my_list)):
    if my_min <= my_list[i] <= my_max:
        res.append(i)

print(res)
