n = int(input())
s = input()
s = list(s)
head = 0
tail = len(s)-1
a = 0
g = 0
c = 0
t = 0
d = 0
for i in range(n):
    if s[tail] == 'A' and a < (n/4):
        a = a+1
        #print(str(a) +'A' )
        tail=tail-1
        print(tail)
    elif s[tail] == 'G' and g < (n / 4):
        g = g + 1
        #print(str(g)+'G')
        tail = tail - 1
    elif s[tail] == 'C' and c < (n / 4):
        c = c + 1
        #print(str(c)+'C')
        tail = tail - 1
        print(str(tail)+"Tail")
    elif s[tail] == 'T' and t < (n / 4):
        t = t + 1
        #print(str(t)+'T')
        tail = tail - 1
    if (a or g or c or t) >= (n/4):
        d = tail
        print(d+1)
        break
k = 0
for j in range(len(s)):
    print(c)
    if s[head] == 'A' and a <= (n / 4):
        a = a + 1
        print(a)
        head = head + 1
    elif s[head] == 'G' and g <= (n / 4):
        g = g + 1
        head = head + 1
    elif s[head] == 'C' and c <= (n / 4):
        c = c + 1
        head = head + 1
    elif s[head] == 'T' and t <= (n / 4):
        t = t + 1
        head = head + 1
    if(a >= (n / 4) or g >= (n / 4) or c >= (n / 4) or t >= (n / 4)):
        k = head
        print(k)
        break
r = s[k:d+1]
print(r)
