#Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания

f = open('dzfile.txt', 'r', encoding='utf-8')
b = []
n = []
s = f.readlines()
for i in s:
    i = i[:-1]
    if i .isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        n.append(i)
print(b)
print(n)
n.sort()
b.sort()
mas = n + b
print(mas)
f.close()