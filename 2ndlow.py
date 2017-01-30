n = int(input())
import math
d = []
while n:
    a = input()
    b = float(input())
    d.append([a, b])
    n =n-1
sec = sorted(list(set([marks for (name, marks) in d])))[1]
na=[]
for (name, value) in d:
    if(value == sec):
        na.append(name)
na.sort()
for i in range(len(na)):
    print(na[i])