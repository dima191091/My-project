stroka = input('Строка: ')
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chisla = []
for i in stroka:
    if i in list:
        chisla.append(i)

print(chisla)
