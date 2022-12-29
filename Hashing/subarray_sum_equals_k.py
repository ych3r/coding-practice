"""
Given an integer array nums and an integer k, 
find the number of subarrays whose sum is equal to k.
"""

nums = [1, 2, 1, 2, 1]
k = 3
ans = 4

"""
- Declare a hash map that maps keys to integers
- Declare an answer variable and a curr variable
- Iterate over the input
    - Check the hash map for curr minus the constraint. Add to ans
    - counts[curr] += 1
    - Update curr
"""

from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)

def sol(nums: list, k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        logging.info(f"num: {num}")
        curr += num
        logging.info(f"curr: {curr}")
        ans += counts[curr - k]
        logging.info(f"ans: {ans}, counts[{curr - k}] == {counts[curr - k]}")
        counts[curr] += 1
        logging.info(f"counts[{curr}] == {counts[curr]}\n")

    return ans

assert sol(nums, k) == ans
