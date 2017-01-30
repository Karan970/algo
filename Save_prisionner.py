#!/bin/python3

import sys


n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
crate = []
ma = 0
for crate_i in range(c):
   crate_t = [int(crate_temp) for crate_temp in input().strip().split(' ')]
   crate.append(crate_t)

for i in crate:
    t1 = i[0]
    t2 = i[1]
    if i[0] < n:
        m = t1*t2
    else:
        m = n*i[1]
    if(m>ma):
        box = t1
        b = i
        ma = m
ind = crate.index(b)
del crate[ind]
req = n-box
reqm=0
y =0
flag = True
while req > 0:
    for i in crate:
        if req <= i[0]:
            flag = True
            r1 = req * i[1]
            if r1 > reqm:
                b1 = i
                reqm = r1
        else:
            flag = False
            t1 = req * i[0]
            t2 = ma + t1
            if t2 > y:
                b1 = i
                y = t2
    del crate[crate.index(b1)]
    req = req - i[0]


if flag==True:
    print(ma+reqm)
else:
    print(ma+y)





# your code goes here
