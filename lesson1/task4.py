n, m, k = list(map(int, input('"n m k" = ').split(' ')))

print("Yes" if not(k % n) or not(k % m) else "No")
