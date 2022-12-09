#!/opt/homebrew/bin/python3

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

nums1= [1,2,3,4]
ans1 = [1,3,6,10]
nums2 = [1,1,1,1,1]
ans2 = [1,2,3,4,5]
nums3 = [3,1,2,10,1]
ans3 = [3,4,6,16,17]

def sol(nums: list) -> list:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix

assert sol(nums1) == ans1
assert sol(nums2) == ans2
assert sol(nums3) == ans3