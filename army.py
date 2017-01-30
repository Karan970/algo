import math
n, m = input().split()
s = (int(n) - 1) * (int(n) - 1)
c = math.sqrt(s)
ans = c
for i in range(int(m)+1):
    if i == 3 or i > 3:
      c+= ans

print(int(c))