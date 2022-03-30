a = int(input("введите первое число"))
b = int(input("введите второе число"))

while a < b:
    a += 1
    if a == 0:
        break
    print(a)