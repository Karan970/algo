import re
q = int(input())
for i in range(q):
    s = input()
    pat = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
    req = re.findall(pat, s)
    print(req)
    for link, head in req:
        print(link + ',' + " " + head.strip())


