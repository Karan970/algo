import math
a = input()
n = int(input())
b = list()
for i in range(math.ceil((len(a))/n)):
    b.append(a[:n])
    a = a[n:]
for s in b:
    c = list()
    for i in s:
        if i not in c:
           c.append(i)

    l = ''.join(map(str, c))
    print(l)



