import random

k = [(random.randint(0,100)) for i in range(10)]
a = tuple(k)
print(a)
print('max', max(k), 'min', min(k))