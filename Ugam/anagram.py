n = input()
m = input()

def di(s):
    d = {}
    for i in s:
        i.lower()
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(int(di(n)==di(m)))