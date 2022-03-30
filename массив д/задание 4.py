import random

chisla = int(input('Количество чисел: '))
odno_chislo = input('Искомая цифра: ')
print(type(odno_chislo))
list = []
while chisla != 0:
    chisla -= 1
    random_chislo = random.randint(1, 99)
    list.append(random_chislo)
print(list)
count = 0
for i in list:
    if odno_chislo in str(i):
        count += 1
print(count)
