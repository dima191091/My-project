mult = 1
k = (-11, -12, -35, 8, 25, -39)
for i in range(6):
    if i % 2 == 1:
       if k[i] < 0:
        mult *= k[i]
print(mult)

