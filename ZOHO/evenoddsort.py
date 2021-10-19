"""
input:
11
1 3 2 4 6 28 23 13 98 23 23
output:
23 23 23 13 3 1 2 4 6 28 98
sort the odds in Descending, sort the evens in ascending and concatenate
"""
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