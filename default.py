a=input().split()
gp = {}
grp = {}

gp['A'] = [input()for i in range(int(a[0]))]
grp['B'] = [input()for i in range(int(a[1]))]
m = grp['B']
for i in range(len(m)):
    v = gp['A']
    flag=False
    d=[]
    j = 0
    while j != len(v):
          if v[j] == m[i]:
               d . append(j+1)
               j = j+1
               flag=True
          else:
              j=j+1
    if flag == False:
        d.append(-1)
        print(d)
    else:
        for i in range(d):
            print(d[i])
        print()