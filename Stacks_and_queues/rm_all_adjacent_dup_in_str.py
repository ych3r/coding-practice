"""
You are given a string s. 
Continuously remove duplicates (two of the same character beside each other) until you can't anymore. 
Return the final string after this.
"""

s = "abbaca"
ans = "ca"

def sol(s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
    

assert sol(s) == ans