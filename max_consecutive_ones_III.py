#!/opt/homebrew/bin/python3

"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
ans1 = 6
# [1,1,1,0,0,1,1,1,1,1,1]

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
ans2 = 10
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

def sol(nums: list, k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

assert sol(nums1, k1) == ans1
assert sol(nums2, k2) == ans2