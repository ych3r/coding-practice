# Stacks

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

## String problems

- [Valid Parentheses](valid_parentheses.py)
- [Remove All Adjacent Duplicates In String](rm_all_adjacent_dup_in_str.py)

---

# Queues