"""
Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
aka 'What is the shortest distance between any two of the same element'
"""

cards = [1, 2, 6, 2, 1]
ans = 2 # [1, 3]

from collections import defaultdict

def sol(cards: list) -> int:
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i]].append(i)
    ans = float("inf")
    for key in dic:
        arr = dic[key]
        for i in range(len(arr) - 1):
            ans = min(ans, arr[i + 1] - arr[i])
    # print(ans)
    return ans if ans < float("inf") else -1

def sol1(cards: list) -> int:
    dic = defaultdict(int)
    ans = float("inf")
    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i - dic[cards[i]])
        dic[cards[i]] = i
    return ans if ans < float("inf") else -1

assert sol(cards) == ans
assert sol1(cards) == ans