n = int(input("Введите число: "))  # вводим 7-ми значное число
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,n % 10]
chet = 0
nechet = 0

for number in numbers:  #  считаем четные и нечетные цифры
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1

# ответ
if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])