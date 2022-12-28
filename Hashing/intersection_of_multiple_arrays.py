"""
Given a 2D array nums that contains n arrays of distinct integers, 
return a sorted array containing all the numbers that appear in all n arrays.
"""

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
ans = [3, 4]

from collections import defaultdict

def sol(nums: list) -> list:
    counts = defaultdict(int)
    for arr in nums:
        for c in arr:
            counts[c] += 1
    ans = list()
    for key in counts:
        if counts[key] == len(nums):
            ans.append(key)
    return sorted(ans)


assert sol(nums) == ans