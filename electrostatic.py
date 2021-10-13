n = [2, 3]
l = "PN"
m = 2
ans = 0
for i in range(m):
    if l[i] == 'P' and n[i] < 0:
        ans += (n[i] * -1)
    if l[i] == "N" and n[i] > 0:
        ans += (n[i] * -1)
    else:
        ans += n[i]
if ans < 0:
    ans = ans * -1
print(ans*100)

