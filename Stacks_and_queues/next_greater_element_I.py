"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

nums1 = [[4, 1, 2], [2, 4], [1, 3, 5, 2, 4]]
nums2 = [[1, 3, 4, 2], [1, 2, 3, 4], [6, 5, 4, 3, 2, 1, 7]]
ans = [[-1, 3, -1], [3, -1], [7, 7, 7, 7, 7]]

from collections import defaultdict

def sol(nums1: list, nums2: list) -> list:
    dic = {}
    dic = defaultdict(lambda: -1, dic)
    stack = []
    for n in nums2:
        while stack and n > stack[-1]:
            dic[stack.pop()] = n
        stack.append(n)
    ans = []
    for n in nums1:
        ans.append(dic[n])
    return ans

for i in range(len(ans)):
    print(sol(nums1[i], nums2[i]))
    assert sol(nums1[i], nums2[i]) == ans[i]