#!/opt/homebrew/bin/python3

"""
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. 
You cannot use the same index twice.
"""

target = 8
nums = [5, 2, 7, 10, 3, 9]

def sol(nums: list, target: int) -> list:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in dic:
            return [i, dic[target - num]]
        dic[num] = i
    return []


print(sol(nums, target))