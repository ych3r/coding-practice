"""
Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i^{th}i 
th
  day to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.
"""

t1 = [34, 33, 32, 31, 20, 50]
t2 = [40, 35, 32, 37, 50]
a1 = [5, 4, 3, 2, 1, 0]
a2 = [4, 2, 1, 1, 0]

def sol(t: list) -> list:
    stack = []
    ans = [0] * len(t)

    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans

assert sol(t1) == a1
assert sol(t2) == a2