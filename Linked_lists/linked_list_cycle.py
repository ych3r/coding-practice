"""
Given the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n2
head_cycle = n0

n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n7.next = n8
n8.next = n9
head_no_cycle = n7

def sol(head: ListNode) -> bool:
    slow = head
    slow_list = [slow.val]
    fast = head
    fast_list = [fast.val]
    while fast and fast.next:
        fast = fast.next.next
        fast_list.append(fast.val)
        slow = slow.next
        slow_list.append(slow.val)
        print(f"fast: {fast_list}\nslow: {slow_list}")
        if fast == slow:
            return True
    return False

assert sol(head_cycle) == True
assert sol(head_no_cycle) == False