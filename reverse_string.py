#!/opt/homebrew/bin/python3

"""
Write a function that reverses a string. The input string is given as an array of characters s.
Space: O(1)
"""

s1 = ["h","e","l","l","o"]
a1 = ["o","l","l","e","h"]
s2 = ["H","a","n","n","a","h"]
a2 = ["h","a","n","n","a","H"]

def sol(s: list):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
sol(s1)
assert s1 == a1, "wrong"
sol(s2)
assert s2 == a2, "wrong"