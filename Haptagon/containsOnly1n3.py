def check(n):
    for i in str(n):
        c = 0
        if not i.__contains__("1") and not i.__contains__("3"):
            return False
    return True


n = int(input())
for i in range(n - 1, 0, -1):
    if check(i):
        print(i, end=" ")
