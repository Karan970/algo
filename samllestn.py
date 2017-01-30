import math
a = int(input())
n = a
sq = []
flag = True
for i in range(2, int(math.sqrt(n))):
    if (i*i) < int(a/4):
        sq.append(i*i)
    else:
        break
print(sq)
for i in range(2, int(a/4)+1):
    t = a/i
    if t in sq:
        print(i)
        flag = False
        break
if flag:
    print(a)

