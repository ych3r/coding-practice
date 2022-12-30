"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

text = [
    "nlaebolko",
    "loonbalxballpoon",
    "leetcode"
]
ans = [1, 2, 0]

from collections import defaultdict

def sol(text: str) -> int:
    counts = defaultdict(int)
    for c in text:
        counts[c] += 1
    return min(counts['b'], counts['a'], counts['n'], counts['l'] // 2, counts['o'] // 2)


for i in range(len(text)):
    assert sol(text[i]) == ans[i]
