n = int(input())
l = list(map(int,input().split()))
if l.__contains__(0):
    res = -9999999999999999999
    ans = 0
    for i in l:
        if i != 0:
            ans += 1
        else:
            ans = 0
        res = max(ans, res)
    print(res)
else:
    print(0)