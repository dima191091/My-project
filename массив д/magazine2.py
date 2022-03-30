name = input("Введите имя: ")
while not name.isalpha():
    name = input("В имени не может быть цифр. Введите корректное имя: ")
phone = input("Введите телефон: ")
while True:
    if "+" == phone[0] and "+375" == phone[:4] and len(phone) == 13:
        break
    else:
        phone = input("Некорректный телефон. Введите телефон: ")
email = input("Введите почту: ")
while True:
    if "@" in email and "." in email[email.index("@"):]: # проверяет наличие собаки и точки после неё
        break
    else:
        email = input("Некорретная почта. Введите корректную почту: ")

catalog = ["Мяч", "Сетка", "Кроссовки"]
prices = [10, 20, 30]
categories = ["Обычный", "Спортивный", "Профессиональный"]
multiplicatiors = [1, 1.5, 2]

cart = []
while True:

    print("Привет, это магазин спорт-товаров.")
    print("1 - посмотреть каталог\n2 - выйти из магазина")
    choice = input("Введите Ваш выбор: ")
    if choice == "1":
        print("Каталог: ")
        for item in enumerate(catalog):
            print(f"{item[0]+1} - {item[1]}")
        choice_item = input("Выберите товар: ")
        print(f"Этот товар стоит: {prices[int(choice_item)-1]}")
        cart.append(int(choice_item)-1)
    if choice == "2":
        print("Корзина: ")
        sum1 = 0
        for i in cart:
            print(f" {catalog[i]} за {prices[i]}$")
            sum1 += prices[i]
        print(f"Итого: {sum1}")
        last_question = input("Будете брать? д/н ")
        if last_question == "д" or last_question == "да":
            print("Спасибо за покупку")
        else:
            print("Жаль. Приходите ещё.")
        exit("Всегда ждём Вас в нашем магазине.")

        # добавить категории товаров, мультипликаторы к товарам
