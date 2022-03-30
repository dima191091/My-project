price=int(input('введите сумму: '))
coints=(25,10,5,1)
size=len(coints)
j=0
while j<size:
    y,price=divmod(price,coints[j])
    if y>0:
        print(f'{y} чеканных монет номиналом {coints[j]}')
    j+=1




