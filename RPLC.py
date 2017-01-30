t = int(input())
while t:
    f = False
    c = 0
    ans = 0
    res = 0
    flag = True
    n = int(input())
    temp = input().split()
    temp = list(map(int, temp))
    for i in range(n):
        t1 = temp[i]
        if flag == True or ans< 0:
            f = False
            res+= t1
            i= i+1

        if res<0 and res<ans:
            f = False
            flag = False
            ans = res
            i = i+1
        else:
            f = True
            c = 1-ans
            i = i+1
    if f == True:
        print("Scenario #"+str(t)+": "+str(c)+"\n")
    else:
        print("Scenario #" + str(t)+": "+str(1-ans)+"\n")
    t = t-1
