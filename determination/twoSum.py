target = int(input())
nums = list(map(int, input().split()))

# multiple loops
for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# single loop
d = {}
for i, j in enumerate(nums):
    if j not in d:
        d[j] = i
    else:
        print(d[j], i)