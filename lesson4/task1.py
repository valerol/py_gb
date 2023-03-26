n = input("Enter the first list amount: ")
m = input("Enter the second list amount: ")
n_list = list(map(int, input("Enter the first list: ").split()))
m_list = list(map(int, input("Enter the first list: ").split()))

res_list = n_list + m_list
res = set(res_list)

for i in res_list:
    if i not in n_list or i not in m_list:
        res.remove(i)

print(sorted(res))
