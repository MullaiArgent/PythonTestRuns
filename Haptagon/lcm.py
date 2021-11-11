l = list(map(int, input().split()))
i = 2
while True:
    if i % l[0] == 0 and i % l[1] == 0:
        print(i)
        break
    i += 1