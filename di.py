import numpy as np
n = int(input())
dic = {}
while n:
    s = input().split()
    n = n-1
    dic[s[0]] = [s[i]for i in range(1, len(s))]
a = input()
m = list(map(int , dic[a]))
if a in dic.keys():
    l = np.average(m)
    print("%.2f"%l)
else:
    print("invalid user name")
