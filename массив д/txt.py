import os

f = open('tdn.txt', 'w', encoding='utf-8')

s = f.readline()
n = int(s)
lst2 = []
for line in f:
    strs = line.split(' ')
print("strs = ", strs)
for s in strs:
    if s != '':
     lst2 = lst2 + [int(s)]
print("n = ", len(lst2))
print("lst2 = ", lst2)
f.close()
