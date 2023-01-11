"""
Given an integer array nums and an integer k, there is a sliding window of size k that moves from the very left to the very right. 
For each window, find the maximum element in the window.
"""

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
ans = [3, 3, 5, 5, 6, 7]

from collections import deque

def sol(nums: list, k: int) -> list:
    ans = []
    queue = deque()
    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)
        if queue[0] + k == i:
            queue.popleft()
        if i >= k - 1:
            ans.append(nums[queue[0]])
    return ans

assert sol(nums, k) == ans