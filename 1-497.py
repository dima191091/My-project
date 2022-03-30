text = "вывести все четные значения в диапазоне от 1 до 497"
for n in  range(1,498):
    if 0 == n % 2:
        text += str(n) + ''
print(text)
