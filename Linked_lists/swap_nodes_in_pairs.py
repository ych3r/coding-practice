"""
Given the head of a linked list, swap every pair of nodes. 
For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
"""

linked_list = [1, 2, 3, 4, 5, 6]

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(linked_list[0])
p = head
for i in linked_list[1:]:
    p.next = ListNode(i)
    p = p.next

# p = head
# while p:
#     print(p.val)
#     p = p.next
# print("\n")

# --- solution ---

def sol(head: ListNode) -> ListNode:
    # edge case
    if not head or not head.next:
        return head

    dummy = head.next
    prev = None
    while head and head.next:
        if prev:
            prev.next = head.next
        prev = head

        next_node = head.next.next
        head.next.next = head

        head.next = next_node
        head = next_node

    return dummy

head = sol(head)

# --- end of solution ---

p = head
ans = []
while p:
    ans.append(p.val)
    p = p.next

assert ans == [2, 1, 4, 3, 6, 5]