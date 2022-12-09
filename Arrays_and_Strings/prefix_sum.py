#!/opt/homebrew/bin/python3

"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
"""

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
ans = [True, False, True]

def sol1(nums: list, queries: list, limit: int) -> list:
    ans = []
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix) - 1])
    for x, y in queries:
        ans.append(prefix[y] - prefix[x] + nums[x] < limit)
    return ans

assert sol1(nums, queries, limit) == ans

"""
Example 2: 2270. Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section.
The second section should have at least one number.
"""

nums = [10, 4, -8, 7]

def sol2(nums: list) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ans = 0
    for i in range(len(nums) - 1):
        left = prefix[i]
        right = prefix[-1] - nums[i]
        if left >= right:
            ans += 1
    return ans

assert sol2(nums) == 2

def sol3(nums: list) -> int:
    ans = left = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1
        
    return ans

assert sol3(nums) == 2