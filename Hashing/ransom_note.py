"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

ransomNote = ["a", "aa", "aa"]
magazine = ["b", "ab", "aab"]
ans = [False, False, True]

from collections import defaultdict

def sol(ransomNote: str, magazine: str) -> bool:
    dic = defaultdict(int)
    for c in magazine:
        dic[c] += 1
    for c in ransomNote:
        if c in dic.keys() and dic[c] > 0:
            dic[c] -= 1
        else:
            return False
    return True

for i in range(len(ans)):
    assert sol(ransomNote[i], magazine[i]) == ans[i]