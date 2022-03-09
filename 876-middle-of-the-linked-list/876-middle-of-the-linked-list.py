# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        single = head
        if not head.next:
            return head
        double = head.next
        
        while double:
            single = single.next
            double = double.next
            if double:
                double = double.next
        
        return single
        