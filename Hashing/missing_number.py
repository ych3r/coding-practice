"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

nums = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1]]
ans = [2, 2, 8]

def sol(nums: list) -> int:
    nums = set(nums)
    for num in range(len(nums) + 1):
        if num not in nums:
            return num
    return -1

for i in range(len(nums)):
    assert sol(nums[i]) == ans[i]