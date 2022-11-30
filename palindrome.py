#!/opt/homebrew/bin/python3
"""
Return true if a given string is a palindrome, false otherwise.
Use Two-pointers technique.
time: O(n)
space: O(1)
"""
import logging

logging.basicConfig(level=logging.INFO)

test_cases = ["abcdcba", "racecar", "Northeastern"]
test_cases_answer = [True, True, False]

def sol(string):
    logging.info(f"test string is: {string}")
    left = 0
    right = len(string) - 1
    logging.info(f"left pointer: {left} right pointer: {right}")
    while left < right: # O(n)
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
        logging.info(f"left pointer: {left} right pointer: {right}")
    return True

ans = []
for test in test_cases:
    ans.append(sol(test))
assert ans == test_cases_answer, "wrong!"