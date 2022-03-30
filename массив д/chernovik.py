import random

a = tuple()
b = tuple()
c = tuple(a + b)
c = c.count(0)
a = tuple(random.randint(1, 100)for i in range(10))
b = tuple(random.randint(1, 100)for i in range(10))
print(max(a))
print(min(a))
print(c)