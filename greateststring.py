c = ''
c1 = ''
str1 = input().split()
# print(str1)
for i in range(len(str1)-1):
    t1 = str1[i] + str1[i + 1]
    t2 = str1[i + 1] + str1[i]
    c = c+t1
    c1 = c1+t2
    print(c)
    print(c1)
    if int(c1) > int(c):
        str1.sort()



sorted(str1,key=str,reverse= True)
print(str1)
