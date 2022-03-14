# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        slow = head
        if slow.next == None:
            return False
        
        fast = slow.next
        
        while slow != fast:
            
            if slow.next == None:
                return False
            
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                return False
            fast = fast.next.next
        
        return True