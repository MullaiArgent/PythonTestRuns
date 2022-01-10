for i in range(int(input())):
    v = int(input())
    temp = 0
    for j in range(1,v):
        if v%j == 0:
            temp += j
    print(temp)
