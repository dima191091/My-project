import random

N = int(input('Количество элементов массива: '))
arr = [int(input('Введите элемент массива: ')) for i in range(N)]

plus = 0
minus = 0
for i in range(N):
    if arr[i] > 0:
        plus += 1
    elif arr[i] < 0:
        minus += 1
if plus > minus:
    for i in range(minus, plus):
        arr.append(random.randint(-100, -1))
elif plus < minus:
    for i in range(plus, minus):
        arr.append(random.randit(1, 100))

print('положительных элементов :', plus)
print('отрицательных элементов :', minus)
print('массив :', arr)




# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.