#!/opt/homebrew/bin/python3

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

nums1 = [1,12,-5,-6,50,3]
k1 = 4
ans1 = 12.75000

nums2 = [5]
k2 = 1
ans2 = 5.00000

def sol(nums: list, k: int) -> float:
    curr = 0
    for i in range(k):
        curr += nums[i]
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans / k

assert sol(nums1, k1) == ans1
assert sol(nums2, k2) == ans2