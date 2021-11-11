"""
input:
samples
4
output:
s
*a
**m
***p
**l
*e
s

input:
happybirthdaybro
5
output:
h
*a
**p
***p
****y
***b
**i
*r
t
*h
**d
***a
****y
***b
**r
*o

input:
happybirthdaybrohappybirthdaybro
8
output:
h
*a
**p
***p
****y
*****b
******i
*******r
******t
*****h
****d
***a
**y
*b
r
*o
**h
***a
****p
*****p
******y
*******b
******i
*****r
****t
***h
**d
*a
y
*b
**r
***o

Process finished with exit code 0

"""
s = input()
h = int(input())
j = 0
inc = True
dec = False
for i in s:
    print(("*" * j) + i)
    if inc:
        j += 1
        if j == h:
            j -= 1
            dec = True
            inc = False
    if dec:
        j -= 1
        if j == 0:
            dec = False
            inc = True

