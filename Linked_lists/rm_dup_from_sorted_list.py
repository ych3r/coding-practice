"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a1.next = a2
a2.next = a3
head1 = a1

b1 = ListNode(1)
b2 = ListNode(1)
b3 = ListNode(2)
b4 = ListNode(3)
b5 = ListNode(3)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
head2 = b1

def sol(head: ListNode) -> ListNode:
    p = head
    while p and p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head

