n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
city = []
ans = []
if n == m:
    print("0")
    exit(0)
for i in range(n):
    city.append(i)
for i in city:
    min = 100000
    for j in c:
        temp = abs(i-j)
        if temp < min:
            min = temp
        if min == 0:
            break
    ans.append(min)
print(max(ans))