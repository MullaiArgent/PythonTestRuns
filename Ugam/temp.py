n = list(map(int, input().split(",")))
m = list(map(int, input().split(",")))
c = 0
for i in n:
    if i in m:
        c += 1
print(c)

