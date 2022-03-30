import random

a = []
m = 0
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(random.randint(10, 100))
        print(a[i][j], end=' ')
    print()
    m = sum(a[i]) if sum(a[i]) > m else m
print(m)
