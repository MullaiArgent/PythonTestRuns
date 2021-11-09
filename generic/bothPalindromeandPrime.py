"""
print the numbers in the given range which are both palindrome and prime
example 1:
input:
101
300
output:
101
131
151
181
191
"""


def palindrome(n):
    return str(n) == str(n)[::-1]


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


start = int(input())
end = int(input())
for n in range(start, end + 1):
    if palindrome(n) and prime(n):
        print(n)
