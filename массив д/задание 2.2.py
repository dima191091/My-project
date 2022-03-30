a = input()
b = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count1 = 0  # гласные
count2 = 0  # согласные
for i in a:
    if i in b:
        count1 += 1
    else:
        count2 += 1
    if count1 == count2:
        for i in a:
            if i in b:
    print(i)
