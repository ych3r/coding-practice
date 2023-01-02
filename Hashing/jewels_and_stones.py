"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

jewels = ["aA", "z"]
stones = ["aAAbbbb", "ZZ"]
ans = [3, 0]

from collections import defaultdict

def sol(jewels: str, stones: str) -> int:
    dic = defaultdict(int)
    for stone in stones:
        dic[stone] += 1
    ans = 0
    for jewel in jewels:
        ans += dic[jewel]
    return ans

for i in range(len(ans)):
    assert sol(jewels[i], stones[i]) == ans[i]