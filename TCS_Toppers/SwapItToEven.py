"""
given two array, find the minimum number of Swaps required
to make the sum of the both array, is Even.
EXAMPLE 1:
INPUT:
4
1 3 2 2
4
2 9 6 3
OUTPUT:
0
EXPLANATION: Both the Arrays sum is Even so, 0.
EXAMPLE 2:
INPUT:
4
1 4 20 2
4
5 9 6 3
OUTPUT:
1
=============================== THIS CODE ONLY PASSES FEW TEST CASES=======================================
"""

n1 = int(input())
l1 = list(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))
arr1 = 0
arr2 = 0
for i in range(n1):
    arr1 += l1[i]
    arr2 += l2[i]
if arr1 % 2 == 0 and arr2 % 2 == 0:
    print(0)
else:
    if arr1 % 2 != 0 and arr2 % 2 != 0:
        flag = -1
        for i in range(n1):
            if (l1[i] + l2[i]) % 2 == 1:
                flag = 1
                break
        print(flag)
