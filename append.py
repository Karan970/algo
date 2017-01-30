from collections import Counter
s1 = input()
s2 = input()
a = s1
b = s2
k = int(input())
s1 = list(s1)
s2 = list(s2)
f = True
c = 0
t = 0
for i in range(len(s2)):
    if i > len(s1)-1:

        continue
    if s2[i] == s1[i]:
        continue
    else:
        f = False
        t = len(s1)-i
        c = len(s2)-i
        break
if (k == (c+t) and f == False) or (k >= (c+t) and t == len(s1)):
    print("Yes")
if f == False:
    print("NO")
if f == True and len(s1) == len(s2):
    print("Yes")
else:
    if len(s1) > len(s2):
        if k >= sum(Counter(a).values())-sum(Counter(b).values()):
            print("Yes")
            exit(0)
        else:
            print("No")
            exit(0)

    else:
        if set(s1) == set(s2):
            print("Yes")
            exit(0)
        if k == sum(Counter(b).values())-sum(Counter(a).values()):
            print("Yes")
            exit(0)
        else:
            print("No")
