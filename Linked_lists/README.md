# Linked lists

What's **node**?
- A node is an element but with more information

```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    one.next = two
    two.next = three
    head = one

    print(head.val)
    print(head.next.val)
    print(head.next.next.val)
```

**Advantages** and **disadvantages** compared to arrays:

Advantage: you can add and remove elements at any position in O(1).
Disadvantage: there's no random access.

**Mechanics**

- When you assign a pointer to an existing linked list node, the pointer refers to the object in memory.

## Fast and slow pointers

## Reversing a linked list
