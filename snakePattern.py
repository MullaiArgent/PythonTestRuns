# Snack Pattern

string = input()
snack = int(input()) + 1
ans = ""
i = 0
for _ in range(0, snack):
    for char in range(i, len(string), snack):
        ans += string[char]
    snack -= 2
    print(ans)
    i += 1
print(ans)