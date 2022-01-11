l1 =int(input())
l2 = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a = a1+a2
a.sort()
a.reverse()
for i in a:
    print(i)