# Stacks and queues
## Stacks

A stack is an ordered collection of elements where elements are added and removed from the same end. (LIFO: Last In First Out)

```py
stack = []

stack.append(1)
stack.append(2)

print(stack.pop())
if not stack:
    print("Stack is empty!")
else:
    print(f"Stack is not empty, top is: {stack[-1]}")
```

### String problems

- [Valid Parentheses](valid_parentheses.py)
- [Remove All Adjacent Duplicates In String](rm_all_adjacent_dup_in_str.py)
- [Backspace String Compare](backspace_str_compare.py)
- [Simplify Path](simplify_path.py)
- [Make The String Great](make_the_str_great.py)

---

## Queues

FIFO: First In First Out

```py
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

while queue:
    print(queue.popleft())
    
if not queue:
    print("Queue is empty!")
```

- [Number of Recent Calls](number_of_recent_calls.py)
- [Moving Average from Data Stream](moving_average_from_data_stream.py)

## Monotonic

A monotonic stack or queue is one whose elements are always sorted.

- [Daily Temperatures](daily_temp.py)
- [Sliding Window Maximum](sliding_window_max.py)
- [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](longest_cont_subarr_w_abs_diff_le_limit.py)
- [Next Greater Element I](next_greater_element_I.py)
- [Online Stock Span](online_stock_span.py)