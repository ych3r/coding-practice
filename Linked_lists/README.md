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

### Mechanics

Assignment:
- When you assign a pointer to an existing linked list node, the pointer refers to the object in memory.

```py
ptr = head
head = head.next
head = None
```

Chaining .next:
- For `head.next.next`, everthing before the final `.next` refers to one node.

Traversal:
- Iterating forward.

```py
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans
```
recursively
```py
def get_sum(head):
    if not head:
        return 0
    
    return head.val + get_sum(head.next)
```

### Types

**Singly linked list**
- each node only has a pointer to the next node
- can only move forward

Add an element:
```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add
```

Delete an element:
```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

**Doubly linked list**
- each node also contains a pointer to the previous node
- allows iteration in both directions

```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```

**Linked lists with sentinel nodes**
- Sentinel nodes sit at the start and end of linked lists and are used to make operations and the code needed to execute those operations clearner
- The real head is `head.next` and the real tail is `tail.prev`

```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
```

**Dummy pointers**
- traverse using a "dummy" pointer and to keep `head` at the head

```py
def get_sum(head):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next
    
    # same as before, but we still have a pointer at the head
    return ans
```

## Fast and slow pointers

Two pointers move at different "speeds" during iteration, begin iteration from different locations, or any other abstract difference.

- [example1](example1.py)
- [Linked List Cycle](linked_list_cycle.py)
- [example3](example3.py)
- [Middle of the Linked List](middle_of_the_linked_list.py)

## Reversing a linked list
