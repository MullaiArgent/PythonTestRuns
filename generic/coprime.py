def factors(n):
    ans = []
    for i in range(2, n):
        if n % i == 0:
            ans.append(i)
    return ans
def co_prime(l1, l2):
    d = {}
    for i in l1 + l2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    flag = 0


l = factors