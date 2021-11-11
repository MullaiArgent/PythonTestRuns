"""
reverse each words except 1st n last word
input :
im fine bro
output:
im enif bro
"""
l = list(input().split())
for i in range(1, len(l)-1):
    l[i] = l[i][::-1]
print(*l)

