a = input('количество чисел')
b = input('искомая цифра')
count = 0
import  random
for i in range(int(a)):
    c = random.randint(1,100)
    for j in str(c):
        if j == b:
            count += 1
    print(c)