n = input()
l = list(map(int, input().split()))
d = int(input())
l.sort()
l = l[len(l)-d:]
for i in range(d):
    print(l[i])
