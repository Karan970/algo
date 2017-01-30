mod = 10**9 + 7
numCases = int(input())

for t in range(numCases):
    n = int(input())
    A = list(map(int, input().split()))
    tot = 0
    pre = [(2**(i-1) * A[i]) % mod for i in range(n + 1)]
    pre[0] = A[0]
    print(pre)
    prefix = [0] * (n + 1)
    prefix[0] = A[0]
    print(prefix)
    for i in range(1, n + 1):
        prefix[i] = (prefix[i-1] + pre[i]) % mod
    print(prefix)
    for i in range(1, n + 1):
        num = 2**(n - i)
        partialProduct = (2 * A[i] * num) % mod
        tot += (partialProduct * prefix[i-1]) % mod
        tot %= mod
    print(tot)
