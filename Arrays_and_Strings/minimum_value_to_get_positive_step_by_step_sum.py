#!/opt/homebrew/bin/python3

"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

nums1 = [-3,2,-3,4,2]
ans1 = 5
nums2 = [1,2]
ans2 = 1
nums3 = [1,-2,-3]
ans3 = 5
nums4 = [2,3,5,-5,-1]
ans4 = 1

def sol(nums: list) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    minimum = min(prefix)
    if minimum >= 1:
        return 1
    else:
        return 1 - minimum

assert sol(nums1) == ans1
assert sol(nums2) == ans2
assert sol(nums3) == ans3
assert sol(nums4) == ans4