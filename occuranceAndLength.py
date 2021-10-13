"""
example 1:
input:
4
1 2 1 2
output:
-1
explanation:
the occurance of 1 is 2 and the occurance of 2 is 2, none of em is greater
than the half of the length of the list, so -1
exaple 2:
input:
3
1 2 1
output:
1
explanation:
the occurance of 1 is 2, such that it is higher than the half of the length of the
given list

"""
n = int(input())
l = list(map(int, input().split()))
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
flag = False
val = max(d.values())
for i,j in d.items():
    if j == val:
        if j > n/2:
            flag = True
            print(i)
            break

if not flag:
    print(-1)