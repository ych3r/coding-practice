class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

arr = [5, 4, 2, 1] # [5, 1], [4, 2]
head = ListNode(arr[0])
p = head
for a in arr[1:]:
    p.next = ListNode(a)
    p = p.next
# p = head
# while p:
#     print(p.val)
#     p = p.next

def sol(head: ListNode) -> int:
    slow = head
    fast = head
    ans = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow is at the middle of the linked list
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    while prev:
        print(head.val, prev.val)
        ans = max(ans, head.val + prev.val)
        prev = prev.next
        head = head.next
    print(ans)
    return ans

assert sol(head) == 6