"""
example 1:
input
5
3
output
615
explanation
5 + 55 + 555 = 615
"""

n = int(input())
t = int(input())
out_flag = 0
for i in range(1, t+1):
    in_flag = ""
    for j in range(1, i+1):
        in_flag += str(n)
    out_flag += int(in_flag)
    in_flag = ""
print(out_flag)
