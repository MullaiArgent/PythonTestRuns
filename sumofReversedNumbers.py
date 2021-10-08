"""
input:
n = 234
output:
666

input:
-123
output:
-444
"""
n = input()
if n[0] == "-":
    n = n[1:]
    m = n[::-1]
    print(-int(m) - int(n))
else:
    m = n[::-1]
    print(int(n) - int(m))


