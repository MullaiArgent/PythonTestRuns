n = int(input())
l1 = list(map(int, input().split()))
e = []
o = []
for i in l1:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
e.sort()
o.sort()
o.reverse()
print(*o+e)