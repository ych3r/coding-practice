"""
Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column, 
and R and C are equal if we consider them as 1D arrays.
"""

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
ans = 1

from collections import defaultdict

def sol(grid: list) -> int:
    dic_row = defaultdict(int)
    for row in grid:
        dic_row[tuple(row)] += 1

    for k, v in dic_row.items():
        print(k, v)

    dic_col = defaultdict(int)
    for col_num in range(len(grid[0])):
        tmp_col = []
        for row_num in range(len(grid)):
            tmp_col.append(grid[row_num][col_num])
        dic_col[tuple(tmp_col)] += 1
    
    for k, v in dic_col.items():
        print(k, v)

    ans = 0
    for arr in dic_row:
        ans += dic_row[arr] * dic_col[arr]
    return ans

assert sol(grid) == ans