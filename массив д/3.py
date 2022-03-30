#создать множество и сделать его неизменным,посчитать количество элементов в нем,проверить на дубликаты

a = {'cat', 'dog', 'monkey'}
b_a = frozenset({'cat', 'dog', 'monkey', 123 , 'chak', 'cat', 'dog', 'monkey'})
union = a | b_a
len(b_a)
st = set(b_a)
print(union)
print(len(a|b_a))
print(len(b_a) == len(b_a))
for i in a:
    print(i)