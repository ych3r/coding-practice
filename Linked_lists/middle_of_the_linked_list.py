"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
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
head1 = n1
ans1 = n3

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
head2 = a1
ans2 = a4

def sol(head: ListNode) -> ListNode :
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

assert sol(head1) == ans1
assert sol(head2) == ans2