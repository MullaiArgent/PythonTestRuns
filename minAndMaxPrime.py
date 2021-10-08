"""
print the difference of the minimum and maximum prime numbers with the given range
example 1:
input:
n = 10
m = 20
output:
8
explanation:
11, 13, 17, 19
answer = 19 - 11
hence 8
"""


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
m = int(input())
min_val = 0
max_val = 0
for i in range(n, m+1):
    if prime(i):
        min_val = i
        break
for i in range(m, n, -1):
    if prime(i):
        max_val = i
        break
print(max_val - min_val)

