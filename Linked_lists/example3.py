"""
Example 3: Given the head of a linked list and an integer k, return the k^{th} node from the end.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
head = n1

k = 2
ans = n4

def sol(head: ListNode, k: int) -> ListNode:
    fast = head
    slow = head
    for _ in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

assert sol(head, k) == ans