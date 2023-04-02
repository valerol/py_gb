first_elem = int(input("First number: "))
diff = int(input("Difference: "))
elems_count = int(input("Amount of elements: "))

res_list = [first_elem]

for i in range(1, elems_count):
    res_list.append(first_elem + i * diff)
    first_elem == res_list[i]

print(res_list)
