#!/opt/homebrew/bin/python3

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

s1 = "ace"
t1 = "abcde"
s2 = "aec"
t2 = "fsgegrw"


def sol(s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


assert sol(s1, t1) == True, "wrong"
assert sol(s2, t2) == False, "wrong"