a = [0, -3, 2, 4]
b = 0
c = 0
d = 0
for i in range(len(a)):
    if a[i]%3==0 and a[i]!=0:
        b+=1
        print('1/3:', b)
for i in range(len(a)):
    if a[i]%2==0:
        c+=a[i]
        d+=1
g = c/d
