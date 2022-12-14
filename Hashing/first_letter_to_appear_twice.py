"""
Given a string s, return the first character to appear twice. 
It is guaranteed that the input will have a duplicate character.
"""

s = "abcdeda"

def sol(s: str) -> str:
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return ""

assert sol(s) == "d"
