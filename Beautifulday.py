i,j,k = input().split()
i = int(i)
j = int(j)
c = 0
for x in range(i, j+1):
    rx = str(x)[::-1]
    t =((x-int(rx))/int(k))

    if (t==int(t)):
       c+=1
    else:
       continue
print(c)


