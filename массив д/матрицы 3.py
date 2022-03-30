a = int(input('введите число: '))
b = int(input('введите число: '))
с = 0
try:
    c = a/b
except ZeroDivisionError:
    print('0')
else:
    print(c**2)
finally:
    print('ok')
