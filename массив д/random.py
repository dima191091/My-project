a = [1, 5, 0, 2, 7, 9]
n = len(a)
for i in range(n - 1):
    b = a[i:].index(min(a[i:]))
    a[i], a[b + i] = a[b + i], a[i]

print(a)

