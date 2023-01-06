"""
Example 1: Given the head of a linked list with an odd number of nodes head, 
return the value of the node in the middle.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
head = one

def sol(head: ListNode) -> int:
    arr = list()
    while head:
        arr.append(head.val)
        head = head.next
    return arr[len(arr) // 2]

def real_sol(head: ListNode) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val

assert sol(head) == 3
assert real_sol(head) == 3