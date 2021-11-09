"""space separated chars to str"""


def solve(N, ch):
    a = ""
    for i in ch:
        if i != " ":
            a += i
    return a
