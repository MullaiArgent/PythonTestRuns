"""
n = no. of elements in array
l = space separated elements
k = no. of rotations
example 1:
input:
5
10 20 30 40 50
2
output:
10 40 50 20 30

example 2:
4
10 20 30 40
1
output:
10 40 20 30

example 3:
input:
3
10 20 30
4
output:
10 20 30
"""

n = int(input())
l = list(map(int, input().split()))
k = int(input())
if len(l) <= 2:
    print(*l)
else:
    for i in range(k):
        temp = l.pop(-1)
        l.insert(1, temp)
    for j in l:
        print(j, end=" ")