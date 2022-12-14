"""
Given an integer array nums, find all the numbers x that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
"""

nums = [1, 2, 3, 5, 7, 8, 10, 12]
ans = [5, 10, 12]

def sol(nums: list) -> list:
    ans = []
    nums = set(nums)
    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    return ans

assert sol(nums) == ans
