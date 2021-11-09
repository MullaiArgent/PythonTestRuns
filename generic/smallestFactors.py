"""
from given two val(a, b), print the bth smallest factors of a
example 1:
input:
12 3
output
3
explanation:
the factors of 12 are 1, 2, 3, 4, 6,
"""
l = list(map(int,input().split()))
count = 0
flag = True
for i in range(1, l[0]+1):
    if l[0] % i == 0: # two equals
        count += 1
        if count == l[1]:  # two equals
            flag = False  # one equal
            print(i)

if flag:
    print(-1)