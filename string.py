import itertools
ana = []
for a in itertools.permutations(input()):
    t = ''.join(a)
    ana.append(t)
ana.sort()
print(*ana, sep=' ')