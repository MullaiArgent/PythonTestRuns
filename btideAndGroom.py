def no_of_neighbours(address, houses):
    ans = 0
    try:
        if address[0] - 1 >= 0 and address[1] - 1 >= 0:
            ans += houses[address[0] - 1][address[1] - 1]
    except IndexError:
        pass
    try:
        if address[0] - 1 >= 0:
            ans += houses[address[0] - 1][address[1]]
    except IndexError:
        pass
    try:
        if address[0] - 1 >= 0:
            ans += houses[address[0] - 1][address[1] + 1]
    except IndexError:
        pass
    try:
        if address[1] - 1 >= 0:
            ans += houses[address[0]][address[1] - 1]
    except IndexError:
        pass
    try:
        ans += houses[address[0]][address[1] + 1]
    except IndexError:
        pass
    try:
        if address[1] - 1 >= 0:
            ans += houses[address[0] + 1][address[1] - 1]
    except IndexError:
        pass
    try:
        ans += houses[address[0] + 1][address[1]]
    except IndexError:
        pass
    try:
        ans += houses[address[0] + 1][address[1] + 1]
    except IndexError:
        pass

    return ans


n = list(map(int, input().split()))

mat = []
for i in range(n[0]):
    temp = list(map(int, input().split()))
    mat.append(temp)

d = {}
for i in range(n[0]):
    for j in range(n[1]):
        if mat[i][j] == 1:
            d[str(i) + "" + str(j)] = no_of_neighbours([i, j], mat)

m = -999999999
for i in d.values():
    m = max(m, i)

l = []
for i, j in d.items():
    if j == m:
        l.append(i)
ans = 999999999999999
print(int(min(l)[0])+1, end=":")
print(int(min(l)[1])+1, end=":")
print(d[min(l)])
