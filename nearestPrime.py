"""
print the difference between of sum of the given array and the nearest Prime Number
example 1:
input:
l = 12 28 15 14
output:
2
i.e, the sum is 69, the nearest prime is 71
example 2:
input:
l = 10 20 5 14
output:
4
i.e, the sum is 49, the nearest prime is 53
example 3:
input:
21 22 23 17
output:
0
i.e, the sum is 83, which is prime
"""


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


l = list(map(int, input().split()))
s = sum(l)
ans = 0
while prime(s):
    s += 1
    ans += 1
print(ans)
