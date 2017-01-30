
t = int(input().strip())
for a0 in range(t):
    c = 1
    n = int(input().strip())
    for i in range(n):
        if i%2==0:
            c= c*2
            print(c)
        else:
            c+=1
            print(c)
    print(c)

