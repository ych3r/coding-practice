"""
Given a string s, determine if all characters have the same frequency.
"""

s = ["abacbc", "aaabb"]
ans = [True, False]

from collections import defaultdict

def sol(s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    frequencies = counts.values()
    print(frequencies)
    return len(set(frequencies)) == 1

for i in range(len(s)):
    assert sol(s[i]) == ans[i]

from collections import Counter

def sol1(s: str) -> bool:
    return len(set(Counter(s).values())) == 1

for i in range(len(s)):
    assert sol1(s[i]) == ans[i]
