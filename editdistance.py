t = int(input())

#print(dp)
while t > 0:
    s1 = input()
    s2 = input()
    t1 = list(s1)
    t2 = list(s2)
    w, h = len(s1) + 1, len(s2) + 1
    dp = [[0 for x in range(h)] for y in range(w)]
    for i in range(len(s1)+1):
        dp[i][0] = i
    #print(dp)
    i = 0
    for i in range(len(s2)+1):
        dp[0][i] = i
    i = 0
    #print(dp)
    for i in range(len(s1)):
        for j in range( len(s2)):
            if t1[i] == t2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = (min(dp[i][j], dp[i+1][j], dp[i][j+1])+1)
                #print(dp)
    print(dp[len(s1)][len(s2)])
    t = t-1




