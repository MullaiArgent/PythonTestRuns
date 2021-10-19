"""
pattern printing
explanation:
 for given range of ODD numbers, print given times with first index cycle rotation
input:
5
output:
1 3 5 7 9
3 5 7 9 1
5 7 9 1 3
7 9 1 3 5
9 1 3 5 7
"""


def odd_list(n):
    l = []
    i = 0
    while len(l) != n:
        if i % 2 != 0:
            l.append(i)
        i += 1

    return l


l1 = odd_list(int(input()))
for i in range(len(l1)):
    print(*l1)
    l1 = l1[1:] + [l1[0]]
