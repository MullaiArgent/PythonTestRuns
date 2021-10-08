"""
sum of the two elements which has least possible products of each other
example 1:
input:
5
12 23 34 2 5
output:
7
"""

n = int(input())
l = list(map(int, input().split()))
d = 9999999999
a = 0
b = 0
for i in range(n):
    for j in range(i+1, n):
        if d > l[i]*l[j]:
            d = l[i]*l[j]
            a = l[i]
            b = l[j]
print(a+b)


