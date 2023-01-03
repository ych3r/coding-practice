"""
Given a string s, find the length of the longest substring without repeating characters.
"""

s = ["abcabcbb", "bbbbb", "pwwkew", " ", "au", "dvdf"]
ans = [3, 1, 3, 1, 2, 3] # "abc", "b", "wke"

from collections import defaultdict

def sol(s: str) -> int:
    dic = defaultdict(int)
    ans = 0
    i = 0
    for j in range(len(s)):
        if s[j] in dic:
            i = max(i, dic[s[j]])
        ans = max(ans, j - i + 1)
        dic[s[j]] = j + 1
    return ans

for i in range(len(ans)):
    assert sol(s[i]) == ans[i]