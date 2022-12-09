#!/opt/homebrew/bin/python3
"""
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.
"""
import logging

logging.basicConfig(level=logging.INFO)

nums = [[1, 2, 4, 6, 8, 9, 14, 15], [2, 3, 5]]
target = [13, 6]
ans = [True, True]

def sol(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        logging.info(f"{nums[left]} - {nums[right]}")
        curr = nums[left] + nums[right]
        if curr == target:
            logging.info(f"Found it! They're {nums[left]} and {nums[right]}")
            return True
        if curr < target:
            left += 1
        else:
            right -= 1
    return False

res = []
for i in range(len(nums)):
    res.append(sol(nums[i], target[i]))
    assert res[i] == ans[i], "wrong!"