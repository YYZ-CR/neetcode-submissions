# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            future = cur.next
            cur.next = prev
            prev = cur
            cur = future
        f = head
        b = prev
        while b:
            f_next = f.next
            f.next = b
            f = f_next
            b_next = b.next
            b.next = f
            b = b_next
