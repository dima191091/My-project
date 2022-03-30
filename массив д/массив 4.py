a = str(input('введите строку : '))
b = str(input('введите строку :'))
c = 0
try:
    c = a/b
    a = str(input('введите строку: '))
    b = str(input('введите строку: '))
except ZeroDivisionError:
    print('0')
except BaseException:
    print()
finally:
    print()

