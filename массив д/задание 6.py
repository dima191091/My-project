a = input('')
count1 = 0
count2 = 0
for i in enumerate(a):
    if i[1].islower() and a[1 + i[0]: 2 +i[0]].islower():
        count1 += 1
        if i[1].isupper() and a[1 + i[0]: 2 +i[0]].isupper():
            count2 += 1

print(a)

