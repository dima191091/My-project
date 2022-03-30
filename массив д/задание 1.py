# n = int(input("Введите число: "))
#
# suma = 0
# mult = 1
#
# while n > 0:
#     digit = n %
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10
#
# print("Сумма:", suma)
# print("Произведение:", mult)

a = input('Введие число ')
count1 = 0
count2 = 0
for i in a:
    if i % 2!= 0:  # проверяем на четность
        count1 += 1
    else:
        count2 += 1  # проверяем на нечетность

if count1 < count2:  # ищем произведение цифр
    sum = 0
    for i in a:
        sum += int(i)
    else:
        print(input(a[1]) * int(a[2]) * int(a[3]))
