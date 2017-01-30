#!/bin/python3
t1 = 0
t2 = 0
xTreasure,yTreasure = input().strip().split(' ')
xTreasure,yTreasure = [int(xTreasure),int(yTreasure)]
n = int(input().strip())
direction = []
for direction_i in range(n):
   direction_t = [int(direction_temp) for direction_temp in input().strip().split(' ')]
   direction.append(direction_t)
for i in direction:
    t1 += i[0]
for i in direction:
    t2 += i[1]
print(str((xTreasure)-t1)+" "+str(int(yTreasure)-t2))


