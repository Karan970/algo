
a = input()
s = list(a)
u = set(s[i] for i in range(len(s)))
u = list(u)
d = 0
flag = True
for i in range(len(u)):
    c = s.count(u[i])
    if c % 2 == 0 and (d == 1 or 0):
        continue
    else:
         d = d+1
    if d > 1:
        flag = False
        break
if flag == True:
     print('YES')
else:
    print('NO')