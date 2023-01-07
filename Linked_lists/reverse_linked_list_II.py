"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

input = [1, 2, 3, 4, 5]
left = 2
right = 4
output = [1, 4, 3, 2, 5]

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(input[0])
p = head
for n in input[1:]:
    p.next = ListNode(n)
    p = p.next


def sol(head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head

    pre = dummy
    curr = dummy.next

    for _ in range(1, left):
        curr = curr.next
        pre = pre.next

    for _ in range(right - left):
        tmp = curr.next
        curr.next = tmp.next
        tmp.next = pre.next
        pre.next = tmp

    return dummy.next
    


new_head = sol(head, left, right)
ans = []
p = new_head
while p:
    ans.append(p.val)
    p = p.next
print(ans)
assert ans == output