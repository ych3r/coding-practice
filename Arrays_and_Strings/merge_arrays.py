#!/opt/homebrew/bin/python3
"""
Given two sorted integer arrays, return an array that combines both of them and is also sorted.
"""
import logging

logging.basicConfig(level=logging.INFO)

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
merged_arr = [1, 3, 4, 5, 6, 7, 20]

def sol(arr1: list, arr2: list) -> list:
    ans = []
    p1 = p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ans.append(arr1[p1])
            p1 += 1
        else:
            ans.append(arr2[p2])
            p2 += 1
    while p1 < len(arr1):
        ans.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        ans.append(arr2[p2])
        p2 += 1
    logging.info(f"ans: {ans}")
    return ans

assert sol(arr1, arr2) == merged_arr, "wrong!"