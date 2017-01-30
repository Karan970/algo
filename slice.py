s = input()
m = input().split()
n = int(m[0])
a = m[1]
st = (str(s[:n])+a+str(s[n+1:]))
print(st)