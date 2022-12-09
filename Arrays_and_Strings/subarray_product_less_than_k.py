#!/opt/homebrew/bin/python3

"""
Given an array of positive integers nums and an integer k,
return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
"""

nums = [10, 5, 2, 6]
k = 100
ans = 8

def sol(nums: list, k: int) -> int:
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr > k:
            left += 1
            curr //= nums[left]
        ans += right - left + 1
    return ans

assert sol(nums, k) == ans
