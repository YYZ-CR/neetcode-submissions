# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first pass
        l = 1
        cur = head
        while cur.next:
            l += 1
            cur = cur.next
        
        #2nd pass
        if n == l: return head.next

        i = l-n-1
        cur = head
        while i and cur.next:
            cur = cur.next
            i -= 1
        cur.next = cur.next.next
        return head

        