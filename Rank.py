
Rank = {'a': 10, 'b': 9, 'd': 8, 'c': 7, 'k': 6,'l': 5, 'g': 4, 'ng': 3, 'q': 2, 'r': 1}

str1 = input()
str2 = input()
p = list(str1)
q = list(str2)
r = min(len(str1), len(str2))
def comp(m ,n):
    t1 = Rank[m]
    t2 = Rank[n]
    if t1 > t2:
        return 1
    elif t1 == t2:
        return 2
    else:
        return 3
i= 0
for i in range(r):
        c = comp(p[i], q[i])
        if c == 1:
            flag = 0
            print("str1>str2")
            break
        if c == 2:
            flag = 1
            continue
        if c == 3:
            flag = 0
            print('str2>str1')
            break
if flag == 1:
    if len(str1) > len(str2):
        print('str1>str2')
    else:
        print('str2>str1')