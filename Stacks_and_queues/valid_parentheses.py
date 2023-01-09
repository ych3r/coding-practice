"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. 
The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, 
and each closing bracket closes exactly one open bracket.
"""

s = ["({})", "(){}[]", "(]", "({)}"]
ans = [True, True, False, False]

def sol(s: str) -> bool:
    dic = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for c in s:
        if c in dic:
            stack.append(c)
        else:
            if not stack:
                return False
            tmp = stack.pop()
            if dic[tmp] != c:
                return False
    if len(stack) == 0:
        return True

for i in range(len(ans)):
    assert sol(s[i]) == ans[i]