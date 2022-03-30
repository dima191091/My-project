n = int(input('Введите размер таблицы: '))
for i in range(1, n + 1):
    for g in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
        else:
            print(g, end=' ')
    print()

    #вывести числа в таблицу,как по итогу