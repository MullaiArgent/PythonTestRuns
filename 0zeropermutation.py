"""
Example 1:
INPUT:
[0, 2, 1, 5, 3, 4]
OUTPUT:
[0, 1, 2, 4, 5, 3]
EXPLANATION:
The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
"""


def check(num):
    l1 = [x for x in nums]
    for i in range(len(nums)):
        nums[i] = l1[l1[i]]
    return nums


nums = [0, 2, 1, 5, 3, 4]
print(check(nums))
