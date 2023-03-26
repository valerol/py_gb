berries_on_bushes = list(map(int, input("Enter amount of berries in each bush: ").split()))

count = 0

for b in range(-1, len(berries_on_bushes)-1):
    new_count = berries_on_bushes[b] + berries_on_bushes[b-1] + berries_on_bushes[b+1]
    print(berries_on_bushes[b], berries_on_bushes[b-1], berries_on_bushes[b+1])
    if new_count > count:
        count = new_count

print(count)
