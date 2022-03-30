from random import random

a = 5
d = 5
c = []
for i in range(d):
    b = []
    for j in range(a):
        b.append(int(random() * 11))
        print("%3d" % b[j], end='')
        c.append(b)
        print()

    for i in range(a):
        print(" ", end='')

        max_sum = 0
        col = 0
        for i in range(a):
            s = 0
            for j in range(d):
                s += c[j][i]
            print("%3d" % s, end='')
            if s > max_sum:
                max_sum = s
                col = i
        print()
        print(col)



# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.