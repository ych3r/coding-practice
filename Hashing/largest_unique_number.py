"""
Given an integer array nums, return the largest integer that only occurs once. 
If no integer occurs once, return -1.
"""

nums = [
    [5,7,3,9,4,9,8,3,1],
    [9,9,8,8]
]

ans = [
    8,
    -1
]

from collections import defaultdict

def sol(nums: list) -> int:
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    ans = -1
    for k, v in counts.items():
        if v == 1 and k > ans:
            ans = k
    return ans

for i in range(len(nums)):
    assert sol(nums[i]) == ans[i]