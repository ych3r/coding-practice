"""
Given an array of positive integers nums and an integer k. 
Find the number of subarrays with exactly k odd numbers in them.
"""

nums = [1, 1, 2, 1, 1]
k = 3
ans = 2

from collections import defaultdict

def sol(nums: list, k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans

assert sol(nums, k) == ans