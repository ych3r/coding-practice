# Arrays and strings

## Common tricks

### O(n) string building

```py
def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)
```

### Subarrays/substrings

> A contiguous section of an array or string.

If a problem has explicit constraints such as:

- Sum greater than or less than k
- Limits on what is contained, such as the maximum of k unique elements or no duplicates allowed

And/or asks for:

- Minimum or maximum length
- Number of subarrays/substrings
- Max or minimum sum

Think about a sliding window.

If a problem's input is an integer array and you find yourself needing to calculate multiple subarray sums, consider building a prefix sum.

The size of a subarray between `i` and `j` (inclusive) is `j - i + 1`. This is also the number of subarrays that end at `j`, starting from `i` or later.

### subsequences

> A portion of an array/string that keeps the same order but doesn't need to be contiguous.

Dynamic programming is used to solve a lot of subsequence problems.

### subsets

> Any group of elements from the original array or string.

Subsets is used in the backtracking.

examples:

```
# Subarrays
[1, 2, 3, 4]
[1], [1, 2, 3], [3, 4]

# Subsequences
[1, 2, 3, 4]
[1, 3], [4], [], [2, 3]

# Subsets
[1, 2, 3, 4]
[3, 2], [4, 1, 2], [1]
```