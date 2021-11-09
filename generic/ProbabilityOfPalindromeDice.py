"""
n = no of times dice rolled
print the probability of Palindromic outcomes.
Explanation:
    if the no. of times dice thrown is 4, the few possible palindromic outcomes are 1221, 3223, 2222, etc,.
"""
import math


def check(n):
    for letter in str(n):
        if int(letter) > 6:
            return False
    if str(n) == str(n)[::-1]:
        return True
    return False


no_of_throws = int(input())
start = ""
end = ""
for _ in range(no_of_throws):
    start += '1'
for _ in range(no_of_throws):
    end += '6'
ans = 0
for i in range(int(start), int(end) + 1):
    if check(i):
        ans += 1

print(str(math.ceil(ans/math.pow(6, no_of_throws))) + "//" + str(math.pow(6, no_of_throws)/ans))

