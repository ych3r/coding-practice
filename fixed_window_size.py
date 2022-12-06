#!/opt/homebrew/bin/python3

"""
Given an integer array nums and an integer k, 
find the sum of the subarray with the largest sum whose length is k.
"""

k = 4
nums = [3, -1, 4, 12, -8, 5, 6]


def sol(nums: list, k: int) -> int:
    curr = 0
    for i in range(k):
        curr += nums[i]
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans

print(sol(nums, k))