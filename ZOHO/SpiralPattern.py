n = int(input())


def print_mat(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print(" ")


mat = [["." for i in range(n)] for j in range(n)]
fore = True
down = False
back = False
up = False
i = 0
j = 0
while not (i == j == 6):
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
print_mat(mat)