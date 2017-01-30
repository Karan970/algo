tot = []
a = int(input())
for i in range(a):
    temp = input()
    tot.append(temp)
n = int(input())
for i in range(n):
    t1 = input()
    c = tot.count(t1)
    print(c)