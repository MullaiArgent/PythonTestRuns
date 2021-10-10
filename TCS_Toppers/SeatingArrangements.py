m = int(input())
n = int(input())
p = int(input())
c = 0
while m > 0 or p > 0 or n > 0:
    team = 0
    if m > 0:
        m -= 1
        team += 1
    if n > 0:
        n -= 1
        team += 1
    if p > 0:
        p -= 1
        team += 1
    elif m > 0:
        m -= 1
        team += 1
    elif n > 0:
        n = 1
        team += 1

    if team == 3:
        c += 1
print(c)
