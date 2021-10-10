"""under construction"""
base = int(input())
a = int(input())
h = ""
temp = 65
for i in range(a):
    h += chr(temp)
    temp += 1

k = int(input())


def permutations_with_repetition(s):
    for n in range(base ** base):
        yield "".join(s[n // base ** (base - d - 1) % base] for d in range(base))


ans = 0
for i in permutations_with_repetition(h):
    print(i)
    temp = 0
    for j in range(a - 1):
        if i[j] != i[j + 1]:
            temp += 1
    if temp == k:
        ans += 1
print(ans)
