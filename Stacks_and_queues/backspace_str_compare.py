"""
Given two strings s and t, 
return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.
"""

s = "ab#c"
t = "ad#c"
ans = True

def helper(string: str) -> list:
    stack = []
    for c in string:
        if stack and c == '#':
            stack.pop()
        else:
            stack.append(c)
    return stack

def sol(s: str, t: str) -> bool:
    return helper(s) == helper(t)

assert sol(s, t) == ans