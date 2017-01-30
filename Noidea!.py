a = input()
a = list(a)
j=len(a)-1
d=0
i=0
flag=False
while i<len(a):
    if i>=j:
        i=i+1
        j=len(a)-1
    else:
        if a[i] == '1' and a[j] == '1':
            i = i + 1
            j = j - 1
        elif a[i] == '0' and a[j] == '0':
            k = i
            b = a[i:j+1]
            l = b.count('0')
            o = b.count('1')
            if l > o:
                flag = True
                while d < len(b):
                    if b[d] == '0':
                        b[d] = '1'
                        d = d + 1
                        i = i + 1
                    else:
                        b[d] = '0'
                        d = d + 1
                        i = i + 1
                a = a[:k] + b + a[j+1:len(a)]
            else:
                j = j - 1
        else:
            if a[i] == '1':
                i = i + 1
            if a[j] == '1':
                j = j - 1
print(a)