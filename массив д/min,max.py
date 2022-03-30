k = (10, 8, 29, 35, 7)
min = 36
max = 6

for i in (k):
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)
min, max = max, min
print( min, max)
