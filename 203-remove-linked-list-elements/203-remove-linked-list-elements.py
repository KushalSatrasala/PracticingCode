# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        res_head = None
        
        cur_node = head
        prev_node = None
        while cur_node and cur_node.val == val:
            prev_node = cur_node
            cur_node = cur_node.next
        
        if cur_node == None:
            return None
        
        if prev_node != None:
            res_head = prev_node.next
            prev_node.next = None
            prev_node = None
        
        while cur_node != None:
            if cur_node.val == val:
                temp_node = cur_node
                cur_node = cur_node.next
                prev_node.next = cur_node
                temp_node.next = None
                
            else:
                if prev_node == None:
                    res_head = cur_node
                prev_node = cur_node
                cur_node = cur_node.next
        
        return res_head