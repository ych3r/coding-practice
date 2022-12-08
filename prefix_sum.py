#!/opt/homebrew/bin/python3

"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
"""

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
ans = [True, False, True]

def sol(nums: list, queries: list, limit: int) -> list:
    ans = []
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix) - 1])
    for x, y in queries:
        ans.append(prefix[y] - prefix[x] + nums[x] < limit)
    return ans

assert sol(nums, queries, limit) == ans