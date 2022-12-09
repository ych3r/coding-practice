#!/opt/homebrew/bin/python3
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

nums1 = [-4,-1,0,3,10]
ans1 = [0,1,9,16,100]
nums2 = [-7,-3,2,3,11]
ans2 = [4,9,9,49,121]

def sol(nums: list) -> list:
    for i in range(len(nums)):
        nums[i] **= 2
    return sorted(nums)

assert sol(nums1) == ans1
assert sol(nums2) == ans2