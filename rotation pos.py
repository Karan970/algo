u = []
n, k, q = input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
n = len(a)
for i in range(q):
    m = (int(input()))
    print(a[(n-k+m) % n])
