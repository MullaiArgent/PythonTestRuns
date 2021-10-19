"""Longest common prefix"""
def check():
    strings = list(input().split())
    ans = ""
    substring = strings[0][0]
    for i in range(len(strings[0])):
        for j in range(1, len(strings)):
            try:
                if strings[j][i] != substring:
                    return ans
            except IndexError:
                return ans
        ans += substring
        try:
            substring = strings[0][i + 1]
        except:
            return ans
    return ans


print(check())
