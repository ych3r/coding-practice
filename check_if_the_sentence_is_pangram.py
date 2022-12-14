"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

sentences = ["thequickbrownfoxjumpsoverthelazydog", "leetcode"]
ans = [True, False]


def sol(sentence: str) -> bool:
    return len(set(sentence)) == 26


for i in range(len(sentences)):
    assert sol(sentences[i]) == ans[i]