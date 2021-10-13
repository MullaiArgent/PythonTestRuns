"""
print "yes" if a input2 can be created from input2
example 1:
input:
abc
cba
output:
yes
example 2:
input:
abcd
aabd
output:
no
"""
def check(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


if check(input()) == check(input()):
    print('yes')
else:
    print('no')

