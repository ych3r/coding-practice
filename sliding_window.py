#!/opt/homebrew/bin/python3

"""
Example 1: Given an array of positive integers nums and an integer k, 
        find the length of the longest subarray whose sum is less than or equal to k.
"""
k = 8
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
ans = 4

def sol1(nums: list, k: int) -> int:
    left = curr = right = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            left += 1
            curr -= nums[left]
        ans = max(ans, right - left + 1)
    return ans

assert sol1(nums, k) == ans


"""
Example 2: You are given a binary substring s (a string containing only "0" and "1"). 
        An operation involves flipping a "0" into a "1". 
        What is the length of the longest substring containing only "1" after performing at most one operation?
"""
s = "1101100111"
ans = 5

def sol2(s: str) -> int:
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == '0':
            curr += 1
        while curr > 1:
            if s[left] == '0':
                curr -=1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

assert sol2(s) == ans