def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


l1 = list(map(int, input().split()))
for i in range(l1[0], l1[1]):
    if prime(i):
        print(i, end=" ")

