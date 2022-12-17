"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
If there are duplicates in arr, count them separately.
"""

arr = [[1,2,3], [1,1,3,3,5,5,7,7], [1,1,2,2]]
ans = [2, 0, 2]

def sol(arr: list) -> int:
    ans = 0
    arr_hashset = set(arr)
    for n in arr:
        if n + 1 in arr_hashset:
            ans += 1
    return ans

for i in range(len(arr)):
    assert sol(arr[i]) == ans[i]