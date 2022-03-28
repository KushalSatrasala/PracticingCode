# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def revListNodes(start):
            cur = start.next
            prev = start
            start.next = None

            ret_tail = start
            ret_head = None
            
            while cur:
                node_next = cur.next
                cur.next = prev
                prev = cur
                cur = node_next
                
            if ret_head == None:
                ret_head = prev
        
            return ret_head, ret_tail
        
        if not head or k == 1:
            return head
        
        res_head = None
        cur_head = head
        prev_head = None
        prev_tail = None
        
        
        while True:
            i = 0
            cur_node = cur_head
            while cur_node and i < k:
                prev_node = cur_node
                cur_node = cur_node.next
                i += 1
            
            prev_node.next = None

            if i != k:
                if not prev_tail:
                    return head
                prev_tail.next = cur_head
                break
            
            rev_head, rev_tail = revListNodes(cur_head)

            if not res_head:
                res_head = rev_head
                prev_head = rev_head
                prev_tail = rev_tail
            else:
                prev_tail.next = rev_head
                prev_head = rev_head
                prev_tail = rev_tail

            cur_head = cur_node
            if not cur_node:
                break
        return res_head
            