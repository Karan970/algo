A = []
B = []
q = []
Q = int(input().strip())
for a0 in range(Q):
    L, R = input().strip().split(' ')
    L, R = [int(L), int(R)]
    q.append([L, R])
m = 0
for i, j in q:
    if j > m:
        m = j
for i in range(m+1):
    A.append(0)
for i in range(m+1):
    if i == 0:
        continue
    else:
        A[i] = A[i-1] ^ i
        t = A[i]
        B.append(t)
for i, j in q:
    sum = 0
    for k in range(i, j+1):
        sum = sum ^ B[k-1]
    print(sum)
