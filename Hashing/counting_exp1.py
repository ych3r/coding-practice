"""
You are given a string s and an integer k. 
Find the length of the longest substring that contains at most k distinct characters.
"""

s = "eceba"
k = 2
ans = 3

from collections import defaultdict

def sol(s: str, k: int) -> int:
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
    

assert sol(s, k) == ans