import re
j=0
a = input().split(':')
print(a)
b = re.findall('\d+|\D+', a[-1])
a[-1] = b[0]
':'.join(list(map(str, a)))
print(a)
