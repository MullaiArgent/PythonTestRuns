n = list(map(int, input().split(",")))
m = list(map(int, input().split(",")))
d = {}
for i in n:
    d[i] = 0
for i in m:
    if i in n:
        d[i] += 1
for i,j in d.items():
    print(str(i) +"-"+ str(j))


