products = {'мяч': 10, 'сетка': 20, 'кроссовки': 30}
multik = {}

for product in products:
    print(product.capitalize())
user_chois = input('напиши название товара,который хочешь купить: ')
if user_chois in products:
    print(f'окей, вы выбрали {user_chois}\nстоимость: (products[user_chois.lower()]')