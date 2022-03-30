str = input('введите строку')
a = str.split()
print(a)
v = []
for i in a:
    v.append(len(i))
g = v.index(max(v))
print(a[g])