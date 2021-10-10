k = int(input())
l = int(input())
m = int(input())
s = min(k, l)
s1 = m + max(k, l) - s
if s1 >= s:
    p = s
while s1 < s:
    s1 += 2
    s -= 1
p = s
print(p)