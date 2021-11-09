def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()


for _ in range(int(input())):
    n = int(input())
    mat = [['.' for i in range(n)] for j in range(n)]
    if n % 2 == 0:
        fore = True
        down = False
        back = False
        up = False
        i = 0
        j = 0
        if i == 0:
            flag = True
            while flag:
                if fore:
                    if j < n - 1:
                        mat[i][j] = '*'
                        print_mat(mat)
                        j += 1
                    else:
                        fore = False
                        down = True
                if down:
                    if i < n - 1:
                        mat[i][j] = '*'
                        print_mat(mat)
                        i += 1
                    else:
                        down = False
                        back = True
                if back:
                    if j > 0:
                        mat[i][j] = '*'
                        j -= 1
                        print_mat(mat)
                    else:
                        back = False
                        up = True
                if up:
                    if i > 0:
                        mat[i][j] = '*'
                        print_mat(mat)
                        i -= 1
                    else:
                        fore = True
                        up = False
                        flag = False
                        i += 2
                        j += 2
            flag = True
            while flag:
                if fore:
                    if mat[i][j + 2] == ".":
                        mat[i][j] = '*'
                        print_mat(mat)
                        j += 1
                    else:
                        fore = False
                        down = True
                if down:
                    if mat[i + 2][j] == ".":
                        mat[i][j] = '*'
                        print_mat(mat)
                        i += 1
                    else:
                        down = False
                        back = True
                if back:
                    if mat[i - 2][j] == ".":
                        mat[i][j] = '*'
                        j -= 1
                        print_mat(mat)
                    else:
                        back = False
                        up = True
                if up:
                    if mat[i - 2][j] == ".":
                        mat[i][j] = '*'
                        print_mat(mat)
                        i -= 1
                    else:
                        fore = True
                        up = False
                        i += 2
                        j += 2
                if i == j == n/2:
                    flag = False




    else:
        pass

