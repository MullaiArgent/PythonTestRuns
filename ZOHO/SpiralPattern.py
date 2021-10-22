"""
Example 1:
input
2
14
25
output
* * * * * * * * * * * * * *
* . . . . . . . . . . . . *
* . * * * * * * * * * * . *
* . * . . . . . . . . * . *
* . * . * * * * * * . * . *
* . * . * . . . . * . * . *
* . * . * . * * . * . * . *
* . * . * . * * . * . * . *
* . * . * . . . . * . * . *
* . * . * * * * * * . * . *
* . * . . . . . . . . * . *
* . * * * * * * * * * * . *
* . . . . . . . . . . . . *
* * * * * * * * * * * * * *

* * * * * * * * * * * * * * * * * * * * * * * * *
. . . . . . . . . . . . . . . . . . . . . . . . *
* * * * * * * * * * * * * * * * * * * * * * * . *
* . . . . . . . . . . . . . . . . . . . . . * . *
* . * * * * * * * * * * * * * * * * * * * . * . *
* . * . . . . . . . . . . . . . . . . . * . * . *
* . * . * * * * * * * * * * * * * * * . * . * . *
* . * . * . . . . . . . . . . . . . * . * . * . *
* . * . * . * * * * * * * * * * * . * . * . * . *
* . * . * . * . . . . . . . . . * . * . * . * . *
* . * . * . * . * * * * * * * . * . * . * . * . *
* . * . * . * . * . . . . . * . * . * . * . * . *
* . * . * . * . * . * * * . * . * . * . * . * . *
* . * . * . * . * . * . . . * . * . * . * . * . *
* . * . * . * . * . * * * * * . * . * . * . * . *
* . * . * . * . * . . . . . . . * . * . * . * . *
* . * . * . * . * * * * * * * * * . * . * . * . *
* . * . * . * . . . . . . . . . . . * . * . * . *
* . * . * . * * * * * * * * * * * * * . * . * . *
* . * . * . . . . . . . . . . . . . . . * . * . *
* . * . * * * * * * * * * * * * * * * * * . * . *
* . * . . . . . . . . . . . . . . . . . . . * . *
* . * * * * * * * * * * * * * * * * * * * * * . *
* . . . . . . . . . . . . . . . . . . . . . . . *
* * * * * * * * * * * * * * * * * * * * * * * * *

explanation:
First line is the number of Test Cases
second line is the Iteration Value, if it is Even Print Square Patter else print Spiral Pattern
"""
for _ in range(int(input())):
    n = int(input())

    def print_mat(mat):
        for i in range(n):
            for j in range(n):
                print(mat[i][j], end=" ")
            print(" ")

    mat = [["." for i in range(n)] for j in range(n)]

    if n % 2 != 0:
        fore = True
        down = False
        back = False
        up = False
        i = 0
        j = 0
        while not (i == j == n//2):
            if fore:
                if i != 0:
                    if i < n and j + 3 < n:
                        if mat[i][j + 2] != "*":
                            j += 1
                            mat[i][j] = "*"

                        else:
                            fore = False
                            down = True
                    else:
                        fore = False
                        down = True
                else:
                    if j < n:
                        mat[i][j] = "*"
                        j += 1
                    else:
                        fore = False
                        down = True
            if down:
                if j != n:
                    if i + 3 < n and j < n:
                        if mat[i + 2][j] != "*":
                            i += 1
                            mat[i][j] = "*"
                        else:
                            down = False
                            back = True
                    else:
                        down = False
                        back = True
                else:
                    if i < n:
                        mat[i][j-1] = "*"
                        i += 1
                    else:
                        down = False
                        back = True
            if back:
                if i != n:
                    if i < n and j > 0:
                        if mat[i][j - 2] != "*":
                            j -= 1
                            mat[i][j] = "*"

                        else:
                            back = False
                            up = True
                    else:
                        back = False
                        up = True
                else:
                    if j != 0:
                        mat[i-1][j-1] = "*"
                        j -= 1
                    else:
                        back = False
                        up = True
            if up:
                if mat[i-2][j] != "*":
                    i -= 1
                    mat[i][j] = "*"
                else:
                    up = False
                    fore = True
        mat[n//2][n//2] = "*"
    else:
        def make(i, j, r, n):
            if r != 0:
                for f in range((n - (r * 2)) - 1):
                    mat[i][j] = "*"
                    j += 1
                for d in range((n - (r * 2)) - 1):
                    mat[i][j] = "*"
                    i += 1
                for b in range((n - (r * 2)) - 1):
                    mat[i][j] = "*"
                    j -= 1
                for u in range((n - (r * 2)) - 1):
                    mat[i][j] = "*"
                    i -= 1
            else:
                for f in range(n-1):
                    mat[i][j] = "*"
                    j += 1

                for d in range(n-1):
                    mat[i][j] = "*"
                    i += 1

                for b in range(n-1):
                    mat[i][j] = "*"
                    j -= 1

                for u in range(n-1):
                    mat[i][j] = "*"
                    i -= 1

        for i in range(n):
            for j in range(n):
                if i == j:
                    if (i == 0 and j == 0) or (i % 2 == 0 and j % 2 == 0):
                        make(i, j, j, n)
    print_mat(mat)
