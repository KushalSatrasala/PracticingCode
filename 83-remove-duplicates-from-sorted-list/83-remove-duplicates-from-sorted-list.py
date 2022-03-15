# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = set()
        if not head:
            return head
        
        prev = head
        cur = head.next
        unique.add(prev.val)
        
        while cur:
            if cur.val in unique:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                unique.add(cur.val)
                cur = cur.next
        
        return head