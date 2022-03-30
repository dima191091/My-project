a = input('введите строку')
b = input('введите символ')
c = ''
for i in a:
    if i != b:
        c += i
print('результат', c)