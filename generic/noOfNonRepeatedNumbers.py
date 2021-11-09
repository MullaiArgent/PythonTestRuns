"""
n = starting val
m = ending val
print the number of numbers with in the given range n and m(inclusive) which has no repeated number in it,
(121 has a repeated 1 in it, 2342 has a repeated 2 in it, 2345 has no repeated number)
example 1:
input:
11
15
output:
4
example 2:
101
200
output:
72
"""


def check(n):
    d = {}
    for j in str(n):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    ans = list(set(d.values()))
    if len(ans) >= 2:
        return False
    elif ans[0] == 1:
        return True
    return False


n = int(input())
m = int(input())
if m <= n:
    print("INVALID INPUT")
else:
    ans = 0
    for i in range(n, m + 1):
        if check(i):
            ans += 1
    print(ans)
