seq = input()
word = input()
t = list(word)
c = 0
for i in range(len(seq)-len(word)+1):
    k = 0
    temp = seq[i:len(word)+i]
    for w in t:
        if w in temp:
            k = k+1
        else:
            break
    if k == len(word) and temp!=word:
        c = c+1
print(c)
