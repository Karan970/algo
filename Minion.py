s = input()
l = len(s)
i=0
dictVow = "AEIOU"
player1 = 0
player2 = 0
for i in range(0,l):
    if(s[i] in dictVow):
        player2 += (l-i)
    else:
        player1 += (l-i)

if(player1 == player2):
    print("Draw")
elif(player1 > player2):
    print("Stuart "+str(player1))
else:
    print("Kevin "+str(player2))