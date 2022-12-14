"""
Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). 
Return -1 if there is no pair of numbers with the same digit sum.
"""

nums = [17, 24, 35, 12, 33, 26]
ans = 61 # [2, 5]

from collections import defaultdict

def get_sum(n: int):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def sol(nums: list) -> int:
    groups = defaultdict(list)
    for num in nums:
        groups[get_sum(num)].append(num)
    # test
    for k, v in groups.items():
        print(k, v)
    # end of test
    ans = -1
    for key in groups:
            curr = groups[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])
    print(ans)
    return ans

assert sol(nums) == ans