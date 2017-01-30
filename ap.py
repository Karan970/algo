a = int(input())
str1 = (input().split())
n = len(str1)
a1 = int(str1[0])
temp = list(map(int, str1))
d = (int(str1[n-1])-int(str1[0]))/len(str1)
s = sum(temp)
t = (2*a1)+(n-1)*d
t = t*(n/2)
r = (abs(t-s))
mis = int(str1[n-1])-r
print(mis)