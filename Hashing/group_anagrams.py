"""
Given an array of strings strs, group the anagrams together.
"""

strs = ["eat","tea","tan","ate","nat","bat"]
ans = [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def sol(strs: list) -> list:
    groups = defaultdict(list)
    for s in strs:
        groups[str(sorted(s))].append(s)
    #print(groups.values())
    return groups.values()

for item in sol(strs):
    #print(sorted(item))
    assert sorted(item) in sorted(ans)
